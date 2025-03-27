from django.urls import path
from . import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:id>/products/', views.CategoryProductListView.as_view(), name='category-product-list'),
    path('', lambda request: HttpResponseRedirect('/api/products/')),
]