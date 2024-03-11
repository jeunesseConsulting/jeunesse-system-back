from backend.abstracts.services import AbstractServices

from purchase_order.models import PurchaseOrder, PurchaseOrderProducts

from asgiref.sync import sync_to_async

import datetime

from django.db.models import F

class PurchaseOrderServices(AbstractServices):


    model = PurchaseOrder

    async def purchase_orders_expiring_today():
        orders = await sync_to_async(list)(
            PurchaseOrder.objects.filter(delivery_date__date=datetime.date.today())
        )

        if orders:
            return orders

        return None
        
    async def purchase_orders_expiring_tomorrow():
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        orders = await sync_to_async(list)(
            PurchaseOrder.objects.filter(delivery_date__date=tomorrow)
        )

        if orders:
            return orders

        return None


class PurchaseOrderProductsServices(AbstractServices):


    model = PurchaseOrderProducts

    def filter_by_purchase_order_id(order):
        return PurchaseOrderProducts.objects.filter(purchase_order=order)
    
    @staticmethod
    def product_purchase_summary(product_id):
        purchase_order_products = PurchaseOrderProducts.objects.filter(product__id=product_id)
        purchase_order_ids = purchase_order_products.values_list('purchase_order', flat=True).distinct()
        purchase_orders = PurchaseOrder.objects.filter(id__in=purchase_order_ids).order_by('created_at')

        return purchase_order_products, purchase_orders
