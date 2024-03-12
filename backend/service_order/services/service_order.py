from backend.abstracts.services import AbstractServices

from service_order.models import ServiceOrder

import datetime

from asgiref.sync import sync_to_async


class ServiceOrderServices(AbstractServices):

    model = ServiceOrder

    async def service_orders_expiring_today():
        orders = await sync_to_async(list)(
            ServiceOrder.objects.filter(delivery_forecast__date=datetime.date.today())
        )

        if orders:
            return orders
        
        return None
    
    async def service_orders_expiring_tomorrow():
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        orders = await sync_to_async(list)(
            ServiceOrder.objects.filter(delivery_forecast__date=tomorrow)
        )

        if orders:
            return orders
        
        return None
