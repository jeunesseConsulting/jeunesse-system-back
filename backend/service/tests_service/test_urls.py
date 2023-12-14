from django.test import SimpleTestCase
from django.urls import reverse, resolve

from service.views.service import ServiceView, ServiceDetailView


class TestUrls(SimpleTestCase):


    def test_service_url_is_resolved(self):
        url = reverse('service_view')
        self.assertEquals(resolve(url).func.view_class, ServiceView)

    def test_service_detail_url_is_resolved(self):
        url = reverse('service_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, ServiceDetailView)