# Generated by Django 2.1.3 on 2019-04-15 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0029_auto_20190414_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list_students',
            name='Proimage',
        ),
        migrations.AlterField(
            model_name='image_students',
            name='image',
            field=models.FileField(blank=True, default='default.png', null='True', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 17, 37, 7, 379408), help_text='Please specify english date: <em>YYYY-MM-DD</em>.'),
        ),
    ]
