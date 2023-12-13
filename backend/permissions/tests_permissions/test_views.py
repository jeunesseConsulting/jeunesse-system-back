from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.permissions_url = reverse('permissions_view')
        self.permissions_detail_url = reverse('permissions_detail_view', kwargs={'id':1})

    def test_permissions_view_unauthorized(self):
        response = self.client.get(self.permissions_url)
        self.assertEquals(response.status_code, 401)

    def test_permissions_detail_view_unauthorized(self):
        response = self.client.get(self.permissions_detail_url)
        self.assertEquals(response.status_code, 401)    