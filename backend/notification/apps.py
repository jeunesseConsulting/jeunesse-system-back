from django.apps import AppConfig
from notification.tasks import schedule_send_test
import asyncio
from threading import Thread

class NotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification'

    def ready(self):
        def schedule():
            asyncio.run(schedule_send_test())

        Thread(target=schedule).start()
