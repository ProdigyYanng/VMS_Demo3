from django.urls import path
from . import views

app_name: str = 'controller'

urlpatterns = [
    path('', views.index, name='index'),
    path('CRUD/', views.CRUD, name='CRUD'),

    path('CarInfoAdd/', views.CarInfoAdd, name='CarInfoAdd'),
    path('CarInfoDel/', views.CarInfoDel, name='CarInfoDel'),
    path('CarInfoEdit/', views.CarInfoEdit, name='CarInfoEdit'),

    path('FailureInfoAdd/', views.FailureInfoAdd, name='FailureInfoAdd'),
    path('FailureInfoDel/', views.FailureInfoDel, name='FailureInfoDel'),
    path('FailureInfoEdit/', views.FailureInfoEdit, name='FailureInfoEdit'),

    path('UserInfoAdd/', views.UserInfoAdd, name='UserInfoAdd'),
    path('UserInfoDel/', views.UserInfoDel, name='UserInfoDel'),
    path('UserInfoEdit/', views.UserInfoEdit, name='UserInfoEdit'),

    path('TravelInfoAdd/', views.TravelInfoAdd, name='TravelInfoAdd'),
    path('TravelInfoDel/', views.TravelInfoDel, name='TravelInfoDel'),
    path('TravelInfoEdit/', views.TravelInfoEdit, name='TravelInfoEdit'),

    path('SiteInfoAdd/', views.SiteInfoAdd, name='SiteInfoAdd'),
    path('SiteInfoDel/', views.SiteInfoDel, name='SiteInfoDel'),
    path('SiteInfoEdit/', views.SiteInfoEdit, name='SiteInfoEdit'),

    path('StationInfoAdd/', views.StationInfoAdd, name='StationInfoAdd'),
    path('StationInfoDel/', views.StationInfoDel, name='StationInfoDel'),
    path('StationInfoEdit/', views.StationInfoEdit, name='StationInfoEdit'),

]
