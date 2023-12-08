from django.apps import AppConfig

from threading import Thread

class NotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification'

    def ready(self):
        from notification.tasks import send_expiring_today_service_order, send_expiring_tomorrow_service_order
        import asyncio
        
        async def schedule():
            await asyncio.gather(send_expiring_today_service_order(), send_expiring_tomorrow_service_order())

        def execute_tasks():
            asyncio.run(schedule())

        Thread(target=execute_tasks).start()
