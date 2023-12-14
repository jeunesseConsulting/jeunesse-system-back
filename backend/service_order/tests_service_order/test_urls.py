from django.test import SimpleTestCase
from django.urls import reverse, resolve

from service_order.views.service_order import ServiceOrderView, ServiceOrderDetailView, ServiceOrderPDFView, ServiceOrderReportView, ServiceOrderSummaryView
from service_order.views.pdf import PDFGeneratorView


class TestUrls(SimpleTestCase):


    def test_service_order_url_is_resolved(self):
        url = reverse('service_order_view')
        self.assertEquals(resolve(url).func.view_class, ServiceOrderView)

    def test_service_order_detail_url_is_resolved(self):
        url = reverse('service_order_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, ServiceOrderDetailView)

    def test_service_order_pdf_url_is_resolved(self):
        url = reverse('service_order_pdf_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, ServiceOrderPDFView)

    def test_pdf_generator_url_is_resolved(self):
        url = reverse('pdf_generator_view')
        self.assertEquals(resolve(url).func.view_class, PDFGeneratorView)

    def test_service_order_report_url_is_resolved(self):
        url = reverse('service_order_report_view')
        self.assertEquals(resolve(url).func.view_class, ServiceOrderReportView)

    def test_service_order_summary_url_is_resolved(self):
        url = reverse('service_order_summary_view')
        self.assertEquals(resolve(url).func.view_class, ServiceOrderSummaryView)
