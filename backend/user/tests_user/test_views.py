from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.auth_url = reverse('auth_view')
        self.user_url = reverse('user_view')
        self.user_detail_url = reverse('user_detail_view', kwargs={'id':1})

    def test_auth_view_unauthorized(self):
        response = self.client.post(self.auth_url)
        self.assertEquals(response.status_code, 401)

    def test_user_url_unauthorized(self):
        response = self.client.get(self.user_url)
        self.assertEquals(response.status_code, 401)

    def test_user_detail_url_unauthorized(self):
        response = self.client.get(self.user_detail_url)
        self.assertEquals(response.status_code, 401)