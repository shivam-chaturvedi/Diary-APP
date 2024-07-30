from django.contrib import admin
from django.urls import path
from Store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.get_all),
    path('add',views.store_data),
    path('clear',views.clear_all_data),
]
