from django.urls import path
from .views import PortList
from . import views

urlpatterns = [
    path('portfolios/', PortList.as_view(), name='port-list'),
    path('api/add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('api/get_cart_items/', views.get_cart_items, name='get_cart_items'),
    # Add other URLs as needed
]