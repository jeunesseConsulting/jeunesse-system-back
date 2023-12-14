from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    
    def setUp(self):
        self.client = Client()
        self.vehicle_url = reverse('vehicle_view')
        self.vehicle_detail_url = reverse('vehicle_detail_view', kwargs={'id':1})

    def test_vehicle_view_unauthorized(self):
        response = self.client.get(self.vehicle_url)
        self.assertEquals(response.status_code, 401)

    def test_vehicle_detail_view_unauthorized(self):
        response = self.client.get(self.vehicle_detail_url)
        self.assertEquals(response.status_code, 401)