# Generated by Django 3.2.8 on 2021-10-16 17:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_time', models.DateTimeField()),
                ('bp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_shop.businesspartner')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_shop.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('dt', models.DateTimeField(default=datetime.datetime.now)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_shop.car')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_shop.order')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_shop.carmodel'),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=datetime.datetime.now)),
                ('cost', models.IntegerField()),
                ('bp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_shop.businesspartner')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_shop.carmodel')),
            ],
        ),
    ]