# Generated by Django 2.2.3 on 2019-07-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_city_cityprovince'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='communityArea',
            field=models.IntegerField(default=None),
        ),
    ]
