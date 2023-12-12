from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from notification.serializer import NotificationSerializer
from notification.services.notification import NotificationServices


class NotificationView(AuthenticatedAPIView):

    model_serializer = NotificationSerializer
    model_service = NotificationServices


class NotificationDetailView(AuthenticatedDetailAPIView):

    model_serializer = NotificationSerializer
    model_service = NotificationServices
