from backend.abstracts.services import AbstractServices

from service_order.models import ServiceOrder

import datetime


class ServiceOrderServices(AbstractServices):

    model = ServiceOrder


    def service_orders_expiring_today():
        orders = ServiceOrder.objects.filter(delivery_forecast__date=datetime.date.today())
        return orders
    
    def service_orders_expiring_tomorrow():
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        orders = ServiceOrder.objects.filter(delivery_forecast__date=tomorrow)
        return orders
