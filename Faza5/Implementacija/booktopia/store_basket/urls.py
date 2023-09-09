from django.urls import path
from .views import *

app_name='basket'
urlpatterns = [
    path('', basket_summary, name='basket_summary'),
    path('add/', basket_add, name='basket_add'),
    path('delete/', basket_delete, name='basket_delete'),
    path('update/', basket_update, name='basket_update'),

    path('basketview/', BasketView, name='basket'),
    path('orderplaced/', order_placed, name='order_placed'),
    path('error/', Error.as_view(), name='error'),
    # path('webhook/', views.stripe_webhook),

]