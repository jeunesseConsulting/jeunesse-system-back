from django.urls import path, include

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
]
