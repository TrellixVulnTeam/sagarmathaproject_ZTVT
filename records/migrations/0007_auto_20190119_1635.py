# Generated by Django 2.1.3 on 2019-01-19 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20190116_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 19, 16, 35, 44, 400582), help_text='Please specify english date: <em>YYYY-MM-DD</em>.'),
        ),
    ]
