from rest_framework import serializers
from .models import *

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    # category = MenuCategorySerializer(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = MenuItem
        fields = [
            "id",
            'name',
            'description',
            'price',
            'category',
            "category_name",
            'preparation_time',
            "is_available"
        ]
        extra_kwargs = {
            'category': {'write_only': True}  # Yalnız yazma üçün, oxuma zamanı göstərilməyəcək
        }
        

class TableSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Table
        fields = '__all__'
        extra_fields = ['status_display']

class ReservationSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    
    class Meta:
        model = Reservation
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    table = TableSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        extra_fields = ['status_display']