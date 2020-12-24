# Generated by Django 2.2 on 2020-12-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('Car_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='汽车编号')),
                ('Car_License', models.CharField(max_length=50, verbose_name='汽车牌照')),
                ('Car_Type', models.CharField(max_length=50, verbose_name='车型号')),
                ('Car_Electric_Quantity', models.FloatField(verbose_name='剩余电量')),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('Site_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='场地id')),
                ('Site_Name', models.CharField(max_length=64, verbose_name='场地名称')),
                ('Center_PosX', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='场地中心经度')),
                ('Center_PosY', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='场地中心纬度')),
            ],
        ),
        migrations.CreateModel(
            name='TravelLog',
            fields=[
                ('Record_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='行驶记录编号')),
                ('Start_Time', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('Traveled_Time', models.IntegerField(verbose_name='已运行分钟数')),
                ('Car_id', models.ForeignKey(on_delete=True, to='login.CarInfo')),
                ('Travel_Site', models.ForeignKey(on_delete=True, to='login.SiteInfo')),
            ],
        ),
        migrations.CreateModel(
            name='StationInfo',
            fields=[
                ('Station_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='站点编号')),
                ('Station_Name', models.CharField(max_length=64, verbose_name='站点名称')),
                ('Station_PosX', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='站点经度')),
                ('Station_PosY', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='站点纬度')),
                ('Site_id', models.ForeignKey(on_delete=True, to='login.SiteInfo')),
            ],
        ),
        migrations.CreateModel(
            name='CarFailureLog',
            fields=[
                ('Record_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='记录编号')),
                ('Fault_Time', models.DateTimeField(auto_now_add=True, verbose_name='故障时间')),
                ('Fault_Type', models.CharField(max_length=1024, verbose_name='故障信息')),
                ('Car_id', models.ForeignKey(on_delete=True, to='login.CarInfo')),
                ('Fault_Station', models.ForeignKey(on_delete=True, to='login.StationInfo')),
            ],
        ),
    ]
