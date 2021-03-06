from django.urls import path
from . import views
from .webhooks import webhook_unique

urlpatterns = [
    path('checkout_unique/<int:item_id>/', views.checkout_unique, name='checkout_unique'),
    path('checkout_success_unique/<order_number>/<product_id>', views.checkout_success_unique, name='checkout_success_unique'),
    path('cache_checkout_data_unique/', views.cache_checkout_data_unique, name='cache_checkout_data_unique'),
    path('whu/', webhook_unique, name='webhook_unique'),
]
