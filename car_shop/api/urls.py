from django.urls import path, include

from .views import InvoiceListAPIView

app_name = 'todo-api'
urlpatterns = [

    path('', InvoiceListAPIView.as_view({'get': 'list', 'post': 'create'}), name='list'),

]
