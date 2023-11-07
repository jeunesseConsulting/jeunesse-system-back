from django.urls import path

from roles.views.role import RoleView, RoleDetailView

urlpatterns = [
    path('', RoleView.as_view(), name='role_view'),
    path('/<id>', RoleDetailView.as_view(), name='role_detail_view')
]

