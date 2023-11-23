from django.urls import path

from supplier.views.supplier import SupplierView, SupplierDetailView


urlpatterns = [
    path('', SupplierView.as_view(), name='supplier_view'),
    path('/<id>', SupplierDetailView.as_view(), name='supplier_detail_view'),    
]
