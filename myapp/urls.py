from django.urls import path
from myapp.views import ProductListCreateView, ProductRetrieveUpdateDestroyView, CartListCreateView, CartRetrieveUpdateDestroyView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('carts/', CartListCreateView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-detail'),
]
