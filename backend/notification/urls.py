from django.urls import path

from notification.views.notification import NotificationView, NotificationDetailView


urlpatterns = [
    path('', NotificationView.as_view(), name='notification_view'),
    path('/<id>', NotificationDetailView.as_view(), name='notification_detail_view'),
]

