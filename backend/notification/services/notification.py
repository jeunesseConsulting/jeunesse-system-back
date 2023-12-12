from backend.abstracts.services import AbstractServices

from notification.models import Notification

from django.utils import timezone

from channels.db import database_sync_to_async


class NotificationServices(AbstractServices):


    model = Notification

    @staticmethod
    @database_sync_to_async
    def create_valid_notification(type, message, relationship_key):
        try:
            today_utc_minus_3 = timezone.localdate(timezone.now() - timezone.timedelta(hours=3))
            notification = Notification.objects.filter(
                type=type,
                message=message,
                relationship_key=relationship_key,
                created_at__date=today_utc_minus_3
            ).first()
        except Notification.DoesNotExist:
            notification = None

        if notification:
            return notification
        else:
            notification = Notification.objects.create(
                type=type,
                message=message,
                relationship_key=relationship_key
            )
            return notification
