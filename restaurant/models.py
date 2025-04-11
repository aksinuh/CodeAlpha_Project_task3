from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.PROTECT)
    preparation_time = models.PositiveIntegerField(help_text="Dəqiqələrlə")
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"

class Table(models.Model):
    STATUS_CHOICES = [
        ('AV', 'Mövcud'),
        ('OC', 'İşğal olunub'),
        ('RS', 'Rezerv edilib'),
        ('MA', 'Təmir üçün'),
    ]
    
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AV')
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Masa {self.number}"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    reservation_time = models.DateTimeField()
    party_size = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['reservation_time']

    def __str__(self):
        return f"{self.customer_name} - {self.reservation_time.strftime('%d.%m.%Y %H:%M')}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('PE', 'Gözləyir'),
        ('PR', 'Hazırlanır'),
        ('RE', 'Hazırdır'),
        ('DE', 'Çatdırılıb'),
        ('CA', 'Ləğv edilib'),
    ]
    
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Sifariş #{self.id} - {self.get_status_display()}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True)
    price_at_order = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.price_at_order:
            self.price_at_order = self.menu_item.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity}"
