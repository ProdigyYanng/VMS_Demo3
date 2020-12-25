from django.urls import path
from . import views

app_name: str = 'login'

urlpatterns = [
    path('', views.index, name='index'),
]
