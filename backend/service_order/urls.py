from django.urls import path

from service_order.views.service_order import ServiceOrderView


urlpatterns = [
    path('', ServiceOrderView.as_view(), name='service_order_view'),
]

