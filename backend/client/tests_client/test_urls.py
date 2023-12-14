from django.test import SimpleTestCase
from django.urls import reverse, resolve

from client.views.client import ClientView, ClientDetailView


class TestUrls(SimpleTestCase):

    
    def test_client_url_is_resolved(self):
        url = reverse('client_view')
        self.assertEquals(resolve(url).func.view_class, ClientView)

    def test_client_detail_url_is_resolved(self):
        url = reverse('client_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, ClientDetailView)
