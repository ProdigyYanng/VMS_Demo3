from django.shortcuts import render, HttpResponse
from login import models
from django.db.models import Sum

# Create your views here.

def index(request):
    # for car in all_cars:
    #     print(car)
    #     print(car.pk)
    #     print(car.Car_License)
    #     print(car.Car_Type)
    #     print(car.Car_Electric_Quantity)
    data = {}
    all_cars = models.CarInfo.objects.order_by('-Car_Electric_Quantity')[:5]  # 5个车辆基本信息
    CarsNum = models.CarInfo.objects.all().count()  # 汽车总数
    CarsUsedNum = models.CarInfo.objects.filter(Car_IsUse=True).count()# 汽车使用数
    CarsMileageNum = models.CarInfo.objects.all().aggregate(Sum('Car_Mileage'))['Car_Mileage__sum']# 行驶总里程数
    CarsMileageAverNum = CarsMileageNum / CarsNum # 行驶平均里程数
    CarsTimeNum = models.TravelLog.objects.all().aggregate(Sum('Traveled_Time'))['Traveled_Time__sum'] # 行驶总时长 min
    CarsAverTimeNum = CarsTimeNum / CarsNum # 每辆车平均行驶时长 min
    CarsCanUse = models.CarInfo.objects.filter(Car_IsUse=False).order_by('-Car_Electric_Quantity')[:5]# 所有可约车辆信息

    # FailureRecord = models.CarFailureLog.objects.values('Car_id').distinct()[:5]# 所有故障车辆信息
    all_FailureRecords = models.CarFailureLog.objects.all()[:5] # todo 这里的故障车辆的外键的反向查询的去重操作还没实现 需要仔细研究
    # for record in all_FailureRecords:
    #     print(record.Car_id.Car_License)
        # car = models.CarInfo.objects.get(Car_id=car['Car_id'])
    # CanUsedCars = models.CarInfo.objects.order_by('-Car_Electric_Quantity').filter(Car_IsUse=False)[:5]# 可用车辆
    # for car in CanUsedCars:
    #     print(car.pk)
    #     print(car.Car_License)

    # FailuedCars = # 故障车辆
    # return render(request, 'controller/controller.html', {'all_cars': all_cars})
    return render(request, 'controller/controller.html', context={
        'all_cars': all_cars,
        'CarsNum': CarsNum,
        'CarsUsedNum': CarsUsedNum,
        'CarsMileageNum': CarsMileageNum,
        'CarsMileageAverNum': CarsMileageAverNum,
        'CarsTimeNum': CarsTimeNum,
        'CarsAverTimeNum': CarsAverTimeNum,
        'CarsCanUse': CarsCanUse,
        'all_FailureRecords': all_FailureRecords,

    })
