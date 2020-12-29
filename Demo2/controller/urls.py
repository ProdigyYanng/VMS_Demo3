from django.urls import path
from . import views

app_name: str = 'controller'

urlpatterns = [
    path('', views.index, name='index'),
    path('CRUD/', views.CRUD, name='CRUD'),
]
