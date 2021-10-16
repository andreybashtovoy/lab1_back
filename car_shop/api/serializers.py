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
    car = CarSerializer(many=False, read_only=True)
    order = OrderSerializer(many=False, read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'
