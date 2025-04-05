from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('record/<int:pk>/',views.customer_record,name='record'),
    path('delete-record/<int:pk>/',views.delete_record,name='delete'),
    path('add-record/',views.add_record,name='add-record'),
   
]
