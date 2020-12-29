from django.urls import path
from . import views

app_name: str = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),


    # path('login/', views.login, name='LoginIndex'),
    # path('login/', views.index),
]
