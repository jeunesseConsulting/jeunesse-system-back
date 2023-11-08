from django.urls import path, include

urlpatterns = [
    path('users', include('user.urls'), name='user_app'),
    path('clients', include('client.urls'), name='client_app'),
    path('roles', include('roles.urls'), name='roles_app'),
    path('permissions', include('permissions.urls'), name='permissions_app'),
    path('products', include('product.urls'), name='product_app'),
    path('vehicles', include('vehicle.urls'), name='vehicle_app'),
    path('service-order', include('service_order.urls'), name='service_order_app'),
    path('service', include('service.urls'), name='service_app'),
]
