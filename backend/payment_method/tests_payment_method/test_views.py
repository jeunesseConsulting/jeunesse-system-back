from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.payment_method_url = reverse('payment_method_view')
        self.payment_method_detail_url = reverse('payment_method_detail_view', kwargs={'id':1})

    def test_payment_method_view_unauthorized(self):
        response = self.client.get(self.payment_method_url)
        self.assertEquals(response.status_code, 401)

    def test_payment_method_detail_view_unauthorized(self):
        response = self.client.get(self.payment_method_detail_url)
        self.assertEquals(response.status_code, 401)
