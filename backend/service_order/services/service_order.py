from backend.abstracts.services import AbstractServices

from service_order.models import ServiceOrder

import datetime

from channels.db import database_sync_to_async


class ServiceOrderServices(AbstractServices):

    model = ServiceOrder

    @database_sync_to_async
    def service_orders_expiring_today():
        orders = ServiceOrder.objects.filter(delivery_forecast__date=datetime.date.today())
        return orders
    
    @database_sync_to_async
    def service_orders_expiring_tomorrow():
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        orders = ServiceOrder.objects.filter(delivery_forecast__date=tomorrow)
        return orders
