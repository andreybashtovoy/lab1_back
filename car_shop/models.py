from datetime import datetime

from django.db import models


class BusinessPartner(models.Model):
    """
    Бізнес-партнер, тобто замовник або постачальник
    """
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)


class CarModel(models.Model):
    """
    Модель авто
    """
    name = models.CharField(max_length=12)


class Car(models.Model):
    """
    Конкретне авто зі вказанням артикулу
    """
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    serial = models.CharField(max_length=12)


class Order(models.Model):
    """
    Замовлення на модель авто
    """
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    bp = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE)
    order_time = models.DateTimeField()


class Invoice(models.Model):
    """
    Виконані замовлення зі вказанням ціни продажу
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.IntegerField()
    dt = models.DateTimeField(default=datetime.now)


class Bill(models.Model):
    """
    Закупівля моделей у постачальників
    """
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    dt = models.DateTimeField(default=datetime.now)
    bp = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE)
    cost = models.IntegerField()
