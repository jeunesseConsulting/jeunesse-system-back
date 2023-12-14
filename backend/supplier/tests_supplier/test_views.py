from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.supplier_url = reverse('supplier_view')
        self.supplier_detail_url = reverse('supplier_detail_view', kwargs={'id':1})

    def test_supplier_view_unauthorized(self):
        response = self.client.get(self.supplier_url)
        self.assertEquals(response.status_code, 401)

    def test_supplier_detail_view_unauthorized(self):
        response = self.client.get(self.supplier_detail_url)
        self.assertEquals(response.status_code, 401)