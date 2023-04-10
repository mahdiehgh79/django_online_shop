
from django.urls import path
from .views import order_datail_view

urlpatterns = [
  path('create/', order_datail_view, name='order_detail'),
]
