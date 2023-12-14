from django.urls import path

from roles.views.roles import RoleView, RoleDetailView

urlpatterns = [
    path('', RoleView.as_view(), name='roles_view'),
    path('/<id>', RoleDetailView.as_view(), name='roles_detail_view')
]

