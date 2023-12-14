from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.service_url = reverse('service_view')
        self.service_detail_url = reverse('service_detail_view', kwargs={'id':1})

    def test_service_view_unauthorized(self):
        response = self.client.get(self.service_url)
        self.assertEquals(response.status_code, 401)

    def test_service_detail_view_unauthorized(self):
        response = self.client.get(self.service_detail_url)
        self.assertEquals(response.status_code, 401)