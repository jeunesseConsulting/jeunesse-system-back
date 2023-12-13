from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.purchase_order_url = reverse('purchase_order_view')
        self.purchase_order_detail_url = reverse('purchase_order_detail_view', kwargs={'id':1})

    def test_purchase_order_view_unauthorized(self):
        response = self.client.get(self.purchase_order_url)
        self.assertEquals(response.status_code, 401)

    def test_purchase_order_detail_view_unauthorized(self):
        response = self.client.get(self.purchase_order_detail_url)
        self.assertEquals(response.status_code, 401)
