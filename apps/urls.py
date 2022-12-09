from django.contrib import admin    
from django.urls import path
from .views import index, save, status, atualizar, apagar


urlpatterns = [

    path('', index),   
    path('save/', save, name="save"),
    path('status/<int:id>', status, name='status'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('apagar/<int:id>', apagar, name='apagar'),
]

