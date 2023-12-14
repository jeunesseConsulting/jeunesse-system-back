from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.service_order_url = reverse('service_order_view')
        self.service_order_detail_url = reverse('service_order_detail_view', kwargs={'id':1})
        self.service_order_pdf_url = reverse('service_order_pdf_view', kwargs={'id':1})
        self.pdf_generator_url = reverse('pdf_generator_view')
        self.service_order_report_url = reverse('service_order_report_view')
        self.service_order_summary_url = reverse('service_order_summary_view')

    def test_service_order_view_unauthorized(self):
        response = self.client.get(self.service_order_url)
        self.assertEquals(response.status_code, 401)

    def test_service_order_detail_view_unauthorized(self):
        response = self.client.get(self.service_order_detail_url)
        self.assertEquals(response.status_code, 401)

    def test_service_order_pdf_view_unauthorized(self):
        response = self.client.get(self.service_order_pdf_url)
        self.assertEquals(response.status_code, 401)

    def test_pdf_generator_view_unauthorized(self):
        response = self.client.get(self.pdf_generator_url)
        self.assertEquals(response.status_code, 401)

    def test_service_order_report_view_unauthorized(self):
        response = self.client.get(self.service_order_report_url)
        self.assertEquals(response.status_code, 401)

    def test_service_order_summary_view_unauthorized(self):
        response = self.client.get(self.service_order_summary_url)
        self.assertEquals(response.status_code, 401)