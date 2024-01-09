from django.urls import path
from .views import index, crypt_payment, paypal

urlpatterns = [
    path('', index),
    path('crypt_payment/', crypt_payment),
    path('paypal/', paypal)
]
