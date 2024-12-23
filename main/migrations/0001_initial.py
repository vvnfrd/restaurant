# Generated by Django 5.1.3 on 2024-12-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free', models.BooleanField(default=True, verbose_name='свободный')),
                ('seats', models.PositiveIntegerField(default=4, verbose_name='кол-во мест')),
                ('is_vip', models.BooleanField(default=False, verbose_name='вип статус')),
            ],
            options={
                'verbose_name': 'стол',
                'verbose_name_plural': 'столы',
            },
        ),
    ]
