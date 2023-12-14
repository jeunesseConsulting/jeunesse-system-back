from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.status_url = reverse('status_view')
        self.status_detail_url = reverse('status_detail_view', kwargs={'id':1})

    def test_status_view_unauthorized(self):
        response = self.client.get(self.status_url)
        self.assertEquals(response.status_code, 401)

    def test_status_detail_view_unauthorized(self):
        response = self.client.get(self.status_detail_url)
        self.assertEquals(response.status_code, 401)