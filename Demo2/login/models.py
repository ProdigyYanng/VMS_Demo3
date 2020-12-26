from django.db import models


# Create your models here.
# todo 完成！ 第一步要添加所有的表 make给数据库 参见数据表.xlsx

class CarInfo(models.Model):  # 车辆信息表
    Car_id = models.IntegerField(verbose_name='汽车编号', primary_key=True)
    Car_License = models.CharField(verbose_name='汽车牌照', max_length=50)
    Car_Type = models.CharField(verbose_name='车型号', max_length=50)
    Car_Electric_Quantity = models.FloatField(verbose_name='剩余电量')
    Car_Mileage = models.FloatField(verbose_name='里程数', default=0)
    Car_IsUse = models.BooleanField(verbose_name='车辆是否在使用', default=False)


class CarFailureLog(models.Model):  # 故障记录表
    Record_id = models.IntegerField(verbose_name='记录编号', primary_key=True)
    Fault_Time = models.DateTimeField(verbose_name='故障时间', auto_now_add=True)
    Fault_Type = models.CharField(verbose_name='故障信息', max_length=1024)
    Fault_Station = models.ForeignKey('StationInfo', on_delete=True)  # 故障站点
    Car_id = models.ForeignKey('CarInfo', on_delete=True)  # 故障车辆id


class TravelLog(models.Model):  # 行驶记录表
    Record_id = models.IntegerField(verbose_name='行驶记录编号', primary_key=True)
    Start_Time = models.DateTimeField(verbose_name='开始时间', auto_now_add=True)
    Traveled_Time = models.IntegerField(verbose_name='已运行分钟数')
    Travel_Site = models.ForeignKey('SiteInfo', on_delete=True)  # 行驶场地
    Car_id = models.ForeignKey('CarInfo', on_delete=True)  # 车辆行驶记录id


class SiteInfo(models.Model):  # 场地信息表
    Site_id = models.IntegerField(verbose_name='场地id', primary_key=True)
    Site_Name = models.CharField(verbose_name='场地名称', max_length=64)
    Center_PosX = models.DecimalField(verbose_name='场地中心经度', max_digits=10, decimal_places=6)
    Center_PosY = models.DecimalField(verbose_name='场地中心纬度', max_digits=10, decimal_places=6)


class StationInfo(models.Model):  # 站点信息表
    Station_id = models.IntegerField(verbose_name='站点编号', primary_key=True)
    Site_id = models.ForeignKey('SiteInfo', on_delete=True)  # 所属场地
    Station_Name = models.CharField(verbose_name='站点名称', max_length=64)
    Station_PosX = models.DecimalField(verbose_name='站点经度', max_digits=10, decimal_places=6)
    Station_PosY = models.DecimalField(verbose_name='站点纬度', max_digits=10, decimal_places=6)


class UserInfo(models.Model): # 用户表
    User_id = models.IntegerField(verbose_name='用户编号', primary_key=True)
    User_Name = models.CharField(verbose_name='用户昵称', max_length=64)
    User_Tel = models.CharField(verbose_name='联系方式', max_length=16)
    User_Register_Time = models.DateTimeField(verbose_name="账户注册时间", auto_now_add=True)
    User_Ordered_Car_id = models.ManyToManyField('CarInfo')  # 用户预约的车编号
    User_Identity = models.CharField(verbose_name='用户身份', max_length=16)
