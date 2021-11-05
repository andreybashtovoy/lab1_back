from rest_framework.viewsets import ModelViewSet

from car_shop.models import Invoice
from .serializers import InvoiceSerializer


class InvoiceListAPIView(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
