from django.contrib import admin
from .models import MenuItem, MenuCategory, Table, Reservation, Order, OrderItem


admin.site.register(MenuItem)
admin.site.register(MenuCategory)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(OrderItem)
