# Generated by Django 2.2.3 on 2019-07-09 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190709_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='cityProvince',
        ),
    ]
