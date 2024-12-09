from django.db import models
import uuid

# Модель Цветов
class Flower(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

# Модель Клиентов
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель Заказов
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)#!!!
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)#!!!
    quantity = models.PositiveIntegerField( null=True, blank=True)#!!!
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.flower.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
