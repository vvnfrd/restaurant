# Generated by Django 5.1.3 on 2024-12-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time_from',
            field=models.DateTimeField(verbose_name='бронь с'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_to',
            field=models.DateTimeField(verbose_name='бронь до'),
        ),
    ]
