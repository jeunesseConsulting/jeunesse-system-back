from django.urls import path

from permissions.views.permission import PermissionsView, PermissionsDetailView


urlpatterns = [
    path('', PermissionsView.as_view(), name='permissions_view'),
    path('/<id>', PermissionsDetailView.as_view(), name='permissions_detail_view'),    
]

