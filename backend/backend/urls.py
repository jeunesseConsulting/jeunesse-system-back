from django.urls import path, include

urlpatterns = [
    path('users', include('user.urls'), name='user_app'),
    path('clients', include('client.urls'), name='client_app'),
    path('roles', include('roles.urls'), name='roles_app'),
]
