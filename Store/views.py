from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Store.models import Diary
import json

# Create your views here.
def store_data(request):
    try:
        if(request.method=='POST'):
            data=json.loads(request.body)

            name=data.get('product_name')
            category=data.get('category')
            price=data.get('price')

            entry=Diary.objects.create(name=name,category=category,price=price)
            entry.save()
            return JsonResponse({'message':'success'},status=201)
        return render(request,'index.html')
    except Exception as e:
        return JsonResponse({'error',str(e)},status=400)
    
def get_all(request):
    try:
        if(request.method=='GET'):
            entries = Diary.objects.all()

            context = {
                'products': entries
            }
        return render(request, 'index.html', context)
    
    except Exception as e:
        return JsonResponse({'error':str(e)},status=400)
    
def clear_all_data(req):
    try:
        if(req.method=='POST'):
            Diary.objects.all().delete()
            return JsonResponse({'message':'success'},status=200)
    except Exception as e:
        return JsonResponse({'error':str(e)},status=400)