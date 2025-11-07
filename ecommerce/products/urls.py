from django.urls import path, include
from rest_framework import routers
from .views import (
    ProductViewSet, CategoryViewSet,
    product_list, product_detail,
    add_product, update_product, delete_product
)

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
]
