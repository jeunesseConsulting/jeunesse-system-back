from django.test import SimpleTestCase
from django.urls import reverse, resolve

from payment_method.views.payment_method import PaymentMethodView, PaymentMethodDetailView


class TestUrls(SimpleTestCase):

    
    def test_payment_method_url_is_resolved(self):
        url = reverse('payment_method_view')
        self.assertEquals(resolve(url).func.view_class, PaymentMethodView)

    def test_payment_method_detail_url_is_resolved(self):
        url = reverse('payment_method_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, PaymentMethodDetailView)
