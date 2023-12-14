from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.product_url = reverse('product_view')
        self.product_detail_url = reverse('product_detail_view', kwargs={'id':1})

    def test_product_view_unauthorized(self):
        response = self.client.get(self.product_url)
        self.assertEquals(response.status_code, 401)

    def test_product_detail_view_unauthorized(self):
        response = self.client.get(self.product_detail_url)
        self.assertEquals(response.status_code, 401)