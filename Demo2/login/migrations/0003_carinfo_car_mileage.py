# Generated by Django 2.2 on 2020-12-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='Car_Mileage',
            field=models.FloatField(default=0, verbose_name='里程数'),
        ),
    ]
