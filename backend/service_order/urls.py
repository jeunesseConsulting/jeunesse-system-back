from django.urls import path

from service_order.views.service_order import ServiceOrderView, ServiceOrderDetailView, ServiceOrderPDFView, ServiceOrderReportView


urlpatterns = [
    path('', ServiceOrderView.as_view(), name='service_order_view'),
    path('/<id>', ServiceOrderDetailView.as_view(), name='service_order_detail_view'),
    path('/pdf/<id>', ServiceOrderPDFView.as_view(), name='service_order_pdf_view'),
    path('/v1/report/<initial_date>/<final_date>', ServiceOrderReportView.as_view(), name='service_order_report_view'),
]

