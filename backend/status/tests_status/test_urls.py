from django.test import SimpleTestCase
from django.urls import reverse, resolve

from status.views.status import StatusView, StatusDetailView


class TestUrls(SimpleTestCase):


    def test_status_url_is_resolved(self):
        url = reverse('status_view')
        self.assertEquals(resolve(url).func.view_class, StatusView)

    def test_status_detail_url_is_resolved(self):
        url = reverse('status_detail_view')
        self.assertEquals(resolve(url).func.view_class, StatusDetailView)