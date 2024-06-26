from django.urls import path

from service_order.views.service_order import ServiceOrderView, ServiceOrderDetailView, ServiceOrderPDFView, ServiceOrderReportView, ServiceOrderSummaryView
from service_order.views.pdf import PDFGeneratorView

urlpatterns = [
    path('', ServiceOrderView.as_view(), name='service_order_view'),
    path('/<id>', ServiceOrderDetailView.as_view(), name='service_order_detail_view'),
    path('/pdf/<id>', ServiceOrderPDFView.as_view(), name='service_order_pdf_view'),
    path('/pdf-generator/base64', PDFGeneratorView.as_view(), name='pdf_generator_view'),
    path('/v1/report', ServiceOrderReportView.as_view(), name='service_order_report_view'),
    path('/v1/summary', ServiceOrderSummaryView.as_view(), name='service_order_summary_view'),
]

