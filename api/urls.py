from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlowerViewSet, CustomerViewSet, OrderViewSet
from .report_generator import generate_docx, generate_report

router = DefaultRouter()
router.register(r'flowers', FlowerViewSet, basename='flower')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('generate-report/', generate_report, name='generate_report'),
    path('generate-docx/', generate_docx, name='generate_docx'),
]
