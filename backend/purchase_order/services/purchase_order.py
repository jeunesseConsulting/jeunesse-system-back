from backend.abstracts.services import AbstractServices

from purchase_order.models import PurchaseOrder, PurchaseOrderProducts

from asgiref.sync import sync_to_async

import datetime

class PurchaseOrderServices(AbstractServices):


    model = PurchaseOrder

    async def purchase_orders_expiring_today():
        orders = await sync_to_async(list)(
            PurchaseOrder.objects.filter(delivery_date__date=datetime.date.today())
        )

        if orders:
            return orders
        else:
            return None
        
    async def purchase_orders_expiring_tomorrow():
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        orders = await sync_to_async(list)(
            PurchaseOrder.objects.filter(delivery_date__date=tomorrow)
        )

        if orders:
            return orders
        else:
            return None


class PurchaseOrderProductsServices(AbstractServices):


    model = PurchaseOrderProducts

    def filter_by_purchase_order_id(order):
        return PurchaseOrderProducts.objects.filter(purchase_order=order)

