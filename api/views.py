from rest_framework import viewsets
from .models import Flower, Customer, Order
from .serializers import FlowerSerializer, CustomerSerializer, OrderSerializer

# ViewSet для цветов
class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

# ViewSet для клиентов
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# ViewSet для заказов
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
