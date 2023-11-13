from django.urls import path

from service_order.views.service_order import ServiceOrderView, ServiceOrderDetailView, ServiceOrderPDFView


urlpatterns = [
    path('', ServiceOrderView.as_view(), name='service_order_view'),
    path('/<id>', ServiceOrderDetailView.as_view(), name='service_order_detail_view'),
    path('/pdf/<id>', ServiceOrderPDFView.as_view(), name='service_order_pdf_view'),
]

