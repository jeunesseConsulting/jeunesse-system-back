from django.test import SimpleTestCase
from django.urls import reverse, resolve

from product.views.product import ProductView, ProductDetailView


class TestUrls(SimpleTestCase):


    def test_product_url_is_resolved(self):
        url = reverse('product_view')
        self.assertEquals(resolve(url).func.view_class, ProductView)

    def test_product_detail_url_is_resolved(self):
        url = reverse('product_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)