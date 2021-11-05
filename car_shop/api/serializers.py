from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer
)

from car_shop.models import CarModel, Car, Order, BusinessPartner, Bill, Invoice


class CarModelSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarSerializer(ModelSerializer):
    model = CarModelSerializer(many=False, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class BPSerializer(ModelSerializer):
    class Meta:
        model = BusinessPartner
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    model = CarModelSerializer(many=False, read_only=True)
    bp = BPSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class InvoiceSerializer(ModelSerializer):
    car = PrimaryKeyRelatedField(many=False, queryset=Car.objects.all())
    order = PrimaryKeyRelatedField(many=False, queryset=Order.objects.all())

    class Meta:
        model = Invoice
        fields = '__all__'

