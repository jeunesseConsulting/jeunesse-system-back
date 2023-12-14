from django.test import SimpleTestCase
from django.urls import reverse, resolve

from user.views.user import UserView, UserDetailView
from user.views.auth import AuthorizationTokenView


class TestUrls(SimpleTestCase):


    def test_auth_url_is_resolved(self):
        url = reverse('auth_view')
        self.assertEquals(resolve(url).func.view_class, AuthorizationTokenView)

    def test_user_url_is_resolved(self):
        url = reverse('user_view')
        self.assertEquals(resolve(url).func.view_class, UserView)

    def test_user_detail_view_is_resolved(self):
        url = reverse('user_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, UserDetailView)