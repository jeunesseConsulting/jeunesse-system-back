from django.urls import path

from user.views.user_views import UserView, UserDetailView
from user.views.auth import AuthorizationTokenView


urlpatterns = [
    path('/auth', AuthorizationTokenView.as_view(), name='auth_view'),

    path('', UserView.as_view(), name='user_view'),
    path('/<id>', UserDetailView.as_view(), name='user_detail_view'),
]
