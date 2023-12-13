from django.test import SimpleTestCase
from django.urls import reverse, resolve

from permissions.views.permission import PermissionsView, PermissionsDetailView


class TestUrls(SimpleTestCase):


    def test_permissions_url_is_resolved(self):
        url = reverse('permissions_view')
        self.assertEquals(resolve(url).func.view_class, PermissionsView)

    def test_permissions_detail_url_is_resolved(self):
        url = reverse('permissions_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, PermissionsDetailView)
