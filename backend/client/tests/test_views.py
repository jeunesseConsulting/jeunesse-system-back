from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.client_url = reverse('client_view')
        self.client_detail_url = reverse('client_detail_view', kwargs={'id':1})

    def test_client_view_unauthorized(self):
        response = self.client.get(self.client_url)
        self.assertEquals(response.status_code, 401)

    def test_client_detail_view_unauthorized(self):
        response = self.client.get(self.client_detail_url)
        self.assertEquals(response.status_code, 401)
