from django.shortcuts import render, HttpResponse, redirect
from login import models
from django.db.models import Sum
from datetime import datetime
from django.contrib.auth.decorators import login_required
import time
# Create your views here.


def ClearSession(func): # 60秒后验证失败需要重新登录
    def wrapper(request):
        f = func(request)
        request.session.set_expiry(600)
        return f
    return wrapper


@ClearSession
def index(request):
    # print(request.session.get('user'))
    # request.session.flush()
    # print(request.session.get('user'))
    # print(request)
    # 测试

    username = request.session.get('user')
    if username == None:
        # 说明没有经过验证 跳转到登录
        request.session.flush()
        return redirect('login:index')


    userid = models.UserInfo.objects.filter(UserAccount=username)[0].User_id

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

@ClearSession
def CRUD(request):
    username = request.session.get('user')
    if username == None:
        # 说明没有经过验证 跳转到登录
        request.session.flush()
        return redirect('login:index')

    cars_obj = models.CarInfo.objects.all()
    CarFailureLogs_obj = models.CarFailureLog.objects.all()
    TravelLogs_obj = models.TravelLog.objects.all()
    SiteInfos_obj = models.SiteInfo.objects.all()
    StationInfos_obj = models.StationInfo.objects.all()
    UserInfos_obj = models.UserInfo.objects.all()


    # User_Ordered_Car_id =

    CarsNum = models.CarInfo.objects.all().count()  # 汽车总数
    CarsUsedNum = models.CarInfo.objects.filter(Car_IsUse=True).count()  # 汽车使用数
    CarsMileageNum = models.CarInfo.objects.all().aggregate(Sum('Car_Mileage'))['Car_Mileage__sum']  # 行驶总里程数
    CarsMileageAverNum = CarsMileageNum / CarsNum  # 行驶平均里程数
    CarsTimeNum = models.TravelLog.objects.all().aggregate(Sum('Traveled_Time'))['Traveled_Time__sum']  # 行驶总时长 min
    CarsAverTimeNum = CarsTimeNum / CarsNum  # 每辆车平均行驶时长 min

    data = {
        'cars_obj': cars_obj,
        'CarFailureLogs_obj': CarFailureLogs_obj,
        'TravelLogs_obj': TravelLogs_obj,
        'SiteInfos_obj': SiteInfos_obj,
        'StationInfos_obj': StationInfos_obj,
        'UserInfos_obj': UserInfos_obj,

        'CarsNum': CarsNum,
        'CarsUsedNum': CarsUsedNum,
        'CarsMileageNum': CarsMileageNum,
        'CarsMileageAverNum': round(CarsMileageAverNum, 3),
        'CarsTimeNum': CarsTimeNum,
        'CarsAverTimeNum': round(CarsAverTimeNum, 3),
    }



    return render(request, 'controller/CRUD.html', context=data)

# 新增信息
def CarInfoAdd(request):
    if request.method == 'POST':
        Car_id = models.CarInfo.objects.all().order_by('-Car_id')[0].Car_id + 1
        Car_License = request.POST.get('Car_License')
        Car_Type = request.POST.get('Car_Type')
        Car_Electric_Quantity = request.POST.get('Car_Electric_Quantity')
        Car_Mileage = request.POST.get('Car_Mileage')
        Car_IsUse = request.POST.get('Car_IsUse')
        Car_Current_PosX = request.POST.get('Car_Current_PosX')
        Car_Current_PosY = request.POST.get('Car_Current_PosY')

        models.CarInfo.objects.create(Car_id=Car_id,
                                      Car_License=Car_License,
                                      Car_Type=Car_Type,
                                      Car_Electric_Quantity=Car_Electric_Quantity,
                                      Car_Mileage=Car_Mileage,
                                      Car_IsUse=Car_IsUse,
                                      Car_Current_PosX=Car_Current_PosX,
                                      Car_Current_PosY=Car_Current_PosY)
        return redirect('controller:CRUD')
        # post请求
        # 获取提交的数据
        # 将数据插入到数据库
        # 返回页面重定向到展示信息
        # get请求返回页面，页面包含form表单进行输入
    return render(request, 'controller/CarInfoAdd.html')

def CarInfoDel(request):
    # 获取id
    # 根据id删除数据库数据
    # 返回重定向
    pk = request.GET.get('id')
    models.CarInfo.objects.filter(pk=pk).delete()
    return redirect('controller:CRUD')


def FailureInfoAdd(request):
    if request.method == 'POST':
        Record_id = models.CarFailureLog.objects.all().order_by('-Record_id')[0].Record_id + 1
        Fault_Time = request.POST.get('Fault_Time')
        Fault_Type = request.POST.get('Fault_Type')
        Fault_Station = int(request.POST.get('Fault_Station'))
        Car_id = int(request.POST.get('Car_id'))

        # Station = models.StationInfo.objects.filter(Fault_Station=Fault_Station)[0].Station_id
        # Car = models.CarInfo.objects.filter(Car_id=Car_id)[0].Car_id
        models.CarFailureLog.objects.create(Record_id=Record_id,
                                            Fault_Time=Fault_Time,
                                            Fault_Type=Fault_Type,
                                            Fault_Station_id=Fault_Station,
                                            Car_id_id=Car_id)
        return redirect('controller:CRUD')
    return render(request, 'controller/FailureInfoAdd.html')

def FailureInfoDel(request):
    pk = request.GET.get('id')
    models.CarFailureLog.objects.filter(pk=pk).delete()
    return redirect('controller:CRUD')


def UserInfoAdd(request):
    if request.method == 'POST':
        User_id = models.UserInfo.objects.all().order_by('-User_id')[0].User_id + 1
        User_Name = request.POST.get('User_Name')
        User_Tel = request.POST.get('User_Tel')
        User_Register_Time = request.POST.get('User_Register_Time')
        User_Ordered_Car_id = int(request.POST.get('User_Ordered_Car_id'))
        User_Identity = request.POST.get('User_Identity')
        UserAccount = request.POST.get('UserAccount')
        UserPwd = request.POST.get('UserPwd')

        user = models.UserInfo(User_id=User_id,
                               User_Name=User_Name,
                               User_Tel=User_Tel,
                               User_Register_Time=User_Register_Time,
                               User_Identity=User_Identity,
                               UserAccount=UserAccount,
                               UserPwd=UserPwd)
        user.save()

        user = models.UserInfo.objects.get(User_id=User_id)
        user.User_Ordered_Car_id.set([User_Ordered_Car_id])
        # cars = models.CarInfo.objects.get(Car_id=User_Ordered_Car_id)

        # User_Ordered_Car_id.set()
        # models.UserInfo.objects.create()
        # models.Login_UserInfo_User_Ordered_Car_id.objects.create(userinfo_id=User_id,carinfo_id=User_Ordered_Car_id)
        return redirect('controller:CRUD')
    return render(request, 'controller/UserInfoAdd.html')

def UserInfoDel(request):
    pk = request.GET.get('id')
    models.UserInfo.objects.filter(pk=pk).delete()
    return redirect('controller:CRUD')


def TravelInfoAdd(request):
    if request.method == 'POST':
        Record_id = models.TravelLog.objects.all().order_by('-Record_id')[0].Record_id + 1
        Start_Time = request.POST.get('Start_Time')
        Traveled_Time = round(float(request.POST.get('Traveled_Time')), 2)
        Travel_Site = int(request.POST.get('Travel_Site'))
        Car_id = int(request.POST.get('Car_id'))

        models.TravelLog.objects.create(Record_id=Record_id,
                                            Start_Time=Start_Time,
                                            Traveled_Time=Traveled_Time,
                                            Travel_Site_id=Travel_Site,
                                            Car_id_id=Car_id)
        return redirect('controller:CRUD')
    return render(request, 'controller/TravelInfoAdd.html')

def TravelInfoDel(request):
    pk = request.GET.get('id')
    models.TravelLog.objects.filter(pk=pk).delete()
    return redirect('controller:CRUD')


def SiteInfoAdd(request):
    if request.method == 'POST':
        Site_id = models.SiteInfo.objects.all().order_by('-Site_id')[0].Site_id + 1
        Site_Name = request.POST.get('Site_Name')
        Center_PosX = request.POST.get('Center_PosX')
        Center_PosY = request.POST.get('Center_PosY')

        models.SiteInfo.objects.create(Site_id=Site_id,
                                       Site_Name=Site_Name,
                                       Center_PosX=Center_PosX,
                                       Center_PosY=Center_PosY)
        return redirect('controller:CRUD')
    return render(request, 'controller/SiteInfoAdd.html')

def SiteInfoDel(request):
    pk = request.GET.get('id')
    models.SiteInfo.objects.filter(pk=pk).delete()
    return redirect('controller:CRUD')

def StationInfoAdd(request):
    if request.method == 'POST':
        Station_id = models.StationInfo.objects.all().order_by('-Station_id')[0].Station_id + 1
        Site_id = int(request.POST.get('Site_id'))
        Station_Name = request.POST.get('Station_Name')
        Station_PosX = request.POST.get('Station_PosX')
        Station_PosY = request.POST.get('Station_PosY')

        models.StationInfo.objects.create(Station_id=Station_id,
                                          Site_id_id=Site_id,
                                          Station_Name=Station_Name,
                                          Station_PosX=Station_PosX,
                                          Station_PosY=Station_PosY)
        return redirect('controller:CRUD')
    return render(request, 'controller/StationInfoAdd.html')

def StationInfoDel(request):
    pk = request.GET.get('id')
    models.StationInfo.objects.filter(pk=pk).delete()
    return redirect('controller:CRUD')
