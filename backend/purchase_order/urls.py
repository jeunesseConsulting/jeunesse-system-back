from django.urls import path

from purchase_order.views.purchase_order import PurchaseOrderView


urlpatterns = [
    path('', PurchaseOrderView.as_view(), name='purchase_order_view'),
]
