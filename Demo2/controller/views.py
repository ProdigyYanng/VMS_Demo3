from django.shortcuts import render, HttpResponse, redirect
from login import models
from django.db.models import Sum
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # 测试
    userid = 1

    # for car in all_cars:
    #     print(car)
    #     print(car.pk)
    #     print(car.Car_License)
    #     print(car.Car_Type)
    #     print(car.Car_Electric_Quantity)

    all_cars = models.CarInfo.objects.order_by('-Car_Electric_Quantity')  # 5个车辆基本信息
    Display_Cals = all_cars[:5]  # 展示的车辆
    CarsNum = models.CarInfo.objects.all().count()  # 汽车总数
    CarsUsedNum = models.CarInfo.objects.filter(Car_IsUse=True).count()  # 汽车使用数
    CarsMileageNum = models.CarInfo.objects.all().aggregate(Sum('Car_Mileage'))['Car_Mileage__sum']  # 行驶总里程数
    CarsMileageAverNum = CarsMileageNum / CarsNum  # 行驶平均里程数
    CarsTimeNum = models.TravelLog.objects.all().aggregate(Sum('Traveled_Time'))['Traveled_Time__sum']  # 行驶总时长 min
    CarsAverTimeNum = CarsTimeNum / CarsNum  # 每辆车平均行驶时长 min
    CarsCanUse = models.CarInfo.objects.filter(Car_IsUse=False).order_by('-Car_Electric_Quantity')[:5]  # 所有可约车辆信息

    # FailureRecord = models.CarFailureLog.objects.values('Car_id').distinct()[:5]# 所有故障车辆信息
    all_FailureRecords = models.CarFailureLog.objects.all()
    Display_FailureRecords = all_FailureRecords[:5]  # todo 这里的故障车辆的外键的反向查询的去重操作还没实现 需要仔细研究

    # for record in all_FailureRecords:
    #     print(record.Car_id.Car_License)
    # car = models.CarInfo.objects.get(Car_id=car['Car_id'])
    # CanUsedCars = models.CarInfo.objects.order_by('-Car_Electric_Quantity').filter(Car_IsUse=False)[:5]# 可用车辆
    # for car in CanUsedCars:
    #     print(car.pk)
    #     print(car.Car_License)

    # FailuedCars = # 故障车辆
    # return render(request, 'controller/controller.html', {'all_cars': all_cars})

    UserRegisterTime = models.UserInfo.objects.filter(User_id=userid)  # 用户注册时间
    date = datetime.strftime(UserRegisterTime[0].User_Register_Time, '%Y/%m/%d')
    UserName = models.UserInfo.objects.filter(User_id=userid)[0].User_Name  # 用户昵称
    UserIdentity = models.UserInfo.objects.filter(User_id=userid)[0].User_Identity  # 用户身份
    # print(date)

    return render(request, 'controller/controller.html', context={
        'all_cars': Display_Cals,  # 要展示的车辆
        'CarsNum': CarsNum,
        'CarsUsedNum': CarsUsedNum,
        'CarsMileageNum': CarsMileageNum,
        'CarsMileageAverNum': round(CarsMileageAverNum, 3),
        'CarsTimeNum': CarsTimeNum,
        'CarsAverTimeNum': round(CarsAverTimeNum, 3),
        'CarsCanUse': CarsCanUse,
        'all_FailureRecords': Display_FailureRecords,
        'date': date,
        'UserName': UserName,
        'UserIdentity': UserIdentity,
        'CarsAllInfo': all_cars,
    })


# todo 1、研究一下在管理员控制面板主页上 点击详情按钮就在地图上显示标记****
# todo 2、本文件index函数中date获取的是用户id是1的账户注册时间，后期需要改成从登陆页面传来的注册时间来进行获取用户id
# todo 3、需要增加一个车辆信息修改的页面，背景仍然是蓝色调
# todo 完成！ 4、是否为user需要增加一个用户身份的字段，来显示您的身份
# todo 5、是否需要一个头像字段（img）


def CRUD(request):
    return render(request, 'controller/CRUD.html')
