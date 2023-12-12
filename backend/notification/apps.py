from django.apps import AppConfig

from threading import Thread

import schedule
import time
import pytz

class NotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification'

    def ready(self):
        from notification.tasks import send_expiring_today_service_order, send_expiring_tomorrow_service_order
        from notification.tasks import send_expiring_today_purchase_order, send_expiring_tomorrow_purchase_order
        import asyncio

        tz = pytz.timezone('America/Sao_Paulo')

        async def gather_tasks():
            await asyncio.gather(
                send_expiring_today_service_order(),
                send_expiring_tomorrow_service_order(),
                send_expiring_today_purchase_order(),
                send_expiring_tomorrow_purchase_order(),
            )
            
        def execute_tasks():
            asyncio.run(gather_tasks())

        schedule.every().day.at("14:12").do(lambda: tz.localize(execute_tasks()).astimezone(pytz.utc))
        schedule.every().day.at("12:30").do(lambda: tz.localize(execute_tasks()).astimezone(pytz.utc))
        schedule.every().day.at("16:00").do(lambda: tz.localize(execute_tasks()).astimezone(pytz.utc))

        def run_schedule():
            while True:
                schedule.run_pending()
                time.sleep(5)

        Thread(target=run_schedule).start()
