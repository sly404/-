# Generated by Django 2.2.3 on 2019-07-06 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190706_0953'),
    ]

    operations = [
        migrations.DeleteModel(
            name='communityRanking',
        ),
        migrations.AlterField(
            model_name='customer',
            name='charger',
            field=models.SmallIntegerField(choices=[(2, '普通用户'), (1, '管理员')], default=2),
        ),
    ]
