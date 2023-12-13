from django.test import SimpleTestCase
from django.urls import reverse, resolve

from roles.views.roles import RoleView, RoleDetailView


class TestUrls(SimpleTestCase):


    def test_roles_url_is_resolved(self):
        url = reverse('roles_view')
        self.assertEquals(resolve(url).func.view_class, RoleView)

    def test_roles_detail_url_is_resolved(self):
        url = reverse('roles_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, RoleDetailView)