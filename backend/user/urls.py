from django.urls import path

from user.views.user_views import UserView, UserDetailView

urlpatterns = [
    path('', UserView.as_view(), name='user_view'),
    path('/<id>', UserDetailView.as_view(), name='user_detail_view'),
]
