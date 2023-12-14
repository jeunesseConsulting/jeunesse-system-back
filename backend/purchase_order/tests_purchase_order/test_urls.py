from django.test import SimpleTestCase
from django.urls import reverse, resolve

from purchase_order.views.purchase_order import PurchaseOrderView, PurchaseOrderDetailView


class TestUrls(SimpleTestCase):


    def test_purchase_order_url_is_resolved(self):
        url = reverse('purchase_order_view')
        self.assertEquals(resolve(url).func.view_class, PurchaseOrderView)

    def test_purchase_order_detail_url_is_resolved(self):
        url = reverse('purchase_order_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, PurchaseOrderDetailView)