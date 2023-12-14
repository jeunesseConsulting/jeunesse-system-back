from django.test import SimpleTestCase
from django.urls import reverse, resolve

from supplier.views.supplier import SupplierView, SupplierDetailView


class TestUrls(SimpleTestCase):


    def test_supplier_url_is_resolved(self):
        url = reverse('supplier_view')
        self.assertEquals(resolve(url).func.view_class, SupplierView)

    def test_supplier_detail_url_is_resolved(self):
        url = reverse('supplier_detail_view')
        self.assertEquals(resolve(url).func.view_class, SupplierDetailView)