from django.urls import path, include

from purchase_order.views.status import PurchaseOrderStatusView, PurchaseOrderStatusDetailView


urlpatterns = [
    path('users', include('user.urls'), name='user_app'),
    path('clients', include('client.urls'), name='client_app'),
    path('roles', include('roles.urls'), name='roles_app'),
    path('permissions', include('permissions.urls'), name='permissions_app'),
    path('products', include('product.urls'), name='product_app'),
    path('vehicles', include('vehicle.urls'), name='vehicle_app'),
    path('service-orders', include('service_order.urls'), name='service_order_app'),
    path('services', include('service.urls'), name='service_app'),
    path('payment-method', include('payment_method.urls'), name='payment_method'),
    path('status', include('status.urls'), name='status_app'),
    path('supplier', include('supplier.urls'), name='supplier_app'),
    path('purchase-order', include('purchase_order.urls'), name='purchase_order_app'),
]

urlpatterns += [
    path('purchase-order-status', PurchaseOrderStatusView.as_view(), name='purchase_order_status_view'),
    path('purchase-order-status/<id>', PurchaseOrderStatusDetailView.as_view(), name='purchase_order_status_detail_view'),
]
