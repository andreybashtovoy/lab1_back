from rest_framework.generics import (
    ListAPIView
)

from car_shop.models import Invoice
from .serializers import InvoiceSerializer


class InvoiceListAPIView(ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
