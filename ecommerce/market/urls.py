from django.urls import path
from django.contrib import admin
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]