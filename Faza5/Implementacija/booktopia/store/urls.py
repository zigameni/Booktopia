from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('', all_products, name='all_products'),
    path('<slug:slug>/', product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', category_list, name='category_list')
]
