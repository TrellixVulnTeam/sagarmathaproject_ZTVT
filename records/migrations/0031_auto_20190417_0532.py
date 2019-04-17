# Generated by Django 2.1.3 on 2019-04-16 23:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0030_auto_20190415_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_students',
            name='image',
            field=models.ImageField(default='default.png', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 17, 5, 32, 39, 810099), help_text='Please specify english date: <em>YYYY-MM-DD</em>.'),
        ),
    ]
