from django.urls import path, include

urlpatterns = [
    path('users', include('user.urls'), name='user_app'),
    path('clients', include('client.urls'), name='client_app'),
    path('roles', include('roles.urls'), name='roles_app'),
    path('permissions', include('permissions.urls'), name='permissions_app'),
    path('products', include('product.urls'), name='product_app'),
    path('vehicles', include('vehicle.urls'), name='vehicle_app'),
]
