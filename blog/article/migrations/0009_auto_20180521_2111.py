# Generated by Django 2.0.4 on 2018-05-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20180521_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='status',
            field=models.IntegerField(choices=[(-1, '进行中'), (0, '逾期'), (1, '已完成'), (2, '放弃')], default=-1),
        ),
    ]
