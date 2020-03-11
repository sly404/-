# Generated by Django 2.2.3 on 2019-07-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190709_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='communityPrice',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='charger',
            field=models.SmallIntegerField(choices=[(2, '普通用户'), (1, '管理员')], default=2),
        ),
    ]
