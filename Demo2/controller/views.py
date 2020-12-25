from django.shortcuts import render, HttpResponse
from login import models

# Create your views here.

def index(request):
    all_cars = models.CarInfo.objects.all()
    # for car in all_cars:
    #     print(car)
    #     print(car.pk)
    #     print(car.Car_License)
    #     print(car.Car_Type)
    #     print(car.Car_Electric_Quantity)

    return render(request, 'controller/controller.html', {'all_cars': all_cars})
