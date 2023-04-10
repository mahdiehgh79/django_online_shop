from django.urls import path
from . import views
from products.views import ProductListView

urlpatterns =[
    path('',ProductListView.as_view(), name='product_list'),
    path('aboutus/',views.AboutUsPageView.as_view(), name='aboutus'),
]