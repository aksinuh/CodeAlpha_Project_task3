from django.urls import path
from .views import *

urlpatterns = [
    # Menu Category URLs
    path('menu-categories/', MenuCategoryListCreateView.as_view(), name='menu-category-list'),
    path('menu-categories/<int:pk>/', MenuCategoryRetrieveUpdateDestroyView.as_view(), name='menu-category-detail'),
    
    # Menu Item URLs
    path('menu-items/', MenuItemListCreateView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroyView.as_view(), name='menu-item-detail'),
    
    # Table URLs
    path('tables/', TableListCreateView.as_view(), name='table-list'),
    path('tables/<int:pk>/', TableRetrieveUpdateDestroyView.as_view(), name='table-detail'),
    
    # Reservation URLs
    path('reservations/', ReservationListCreateView.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-detail'),
    
    # Order URLs
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    
    # Order Item URLs
    path('order-items/', OrderItemListCreateView.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', OrderItemRetrieveUpdateDestroyView.as_view(), name='order-item-detail'),
]