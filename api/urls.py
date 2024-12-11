from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlowerViewSet, CustomerViewSet, OrderDetailViewSet, OrderViewSet, SupplierViewSet
from .report_generator import generate_docx, generate_report

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'flowers', FlowerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-details', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate-report/', generate_report, name='generate_report'),
    path('generate-docx/', generate_docx, name='generate_docx'),
]
