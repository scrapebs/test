# Generated by Django 2.0.2 on 2018-03-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20180317_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending_info',
            name='created_date',
            field=models.DateTimeField(verbose_name='%Y-%m-%d %H:%M:%S'),
        ),
    ]
