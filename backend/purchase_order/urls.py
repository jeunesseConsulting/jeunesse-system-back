from django.urls import path

from purchase_order.views.purchase_order import PurchaseOrderView, PurchaseOrderDetailView


urlpatterns = [
    path('', PurchaseOrderView.as_view(), name='purchase_order_view'),
    path('/<id>', PurchaseOrderDetailView.as_view(), name='purchase_order_detail_view'),
]
