from django.urls import path
from . import views

app_name: str = 'controller'

urlpatterns = [
    path('', views.index, name='index'),
    path('CRUD/', views.CRUD, name='CRUD'),

    path('CarInfoAdd/', views.CarInfoAdd, name='CarInfoAdd'),
    path('CarInfoDel/', views.CarInfoDel, name='CarInfoDel'),

    path('FailureInfoAdd/', views.FailureInfoAdd, name='FailureInfoAdd'),
    path('FailureInfoDel/', views.FailureInfoDel, name='FailureInfoDel'),

    path('UserInfoAdd/', views.UserInfoAdd, name='UserInfoAdd'),
    path('UserInfoDel/', views.UserInfoDel, name='UserInfoDel'),

    path('TravelInfoAdd/', views.TravelInfoAdd, name='TravelInfoAdd'),
    path('TravelInfoDel/', views.TravelInfoDel, name='TravelInfoDel'),

    path('SiteInfoAdd/', views.SiteInfoAdd, name='SiteInfoAdd'),
    path('SiteInfoDel/', views.SiteInfoDel, name='SiteInfoDel'),

    path('StationInfoAdd/', views.StationInfoAdd, name='StationInfoAdd'),
    path('StationInfoDel/', views.StationInfoDel, name='StationInfoDel'),

]
