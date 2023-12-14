from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.roles_url = reverse('roles_view')
        self.roles_detail_url = reverse('roles_detail_view', kwargs={'id':1})

    def test_roles_view_unauthorized(self):
        response = self.client.get(self.roles_url)
        self.assertEquals(response.status_code, 401)

    def test_roles_detail_view_unauthorized(self):
        response = self.client.get(self.roles_detail_url)
        self.assertEquals(response.status_code, 401)