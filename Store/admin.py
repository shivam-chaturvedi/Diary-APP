from django.contrib import admin
from Store.models import Diary

# Register your models here.
class diaryAdmin(admin.ModelAdmin):
    list_display=['id','name','category','price']
    ordering=['id']
admin.site.register(Diary,diaryAdmin)