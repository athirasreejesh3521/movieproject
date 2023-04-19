from django.contrib import admin
from django.urls import path
from . import views

app_name='sthiraapp'
urlpatterns = [

    path('', views.service, name='service'),
    path('service/<int:service_id>/', views.detail, name='detail'),
    path('add/', views.add_service, name='add_service'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]