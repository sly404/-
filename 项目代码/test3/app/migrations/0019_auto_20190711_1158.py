# Generated by Django 2.2.3 on 2019-07-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_community_communityarea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentThumbUp',
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentCustomerID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.CharField(default='2019-07-11 03:58:10', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='charger',
            field=models.SmallIntegerField(choices=[(1, '管理员'), (2, '普通用户')], default=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='postTime',
            field=models.CharField(default='2019-07-11 03:58:10', max_length=50),
        ),
    ]
