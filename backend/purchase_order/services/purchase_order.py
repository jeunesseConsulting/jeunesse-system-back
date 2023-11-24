from backend.abstracts.services import AbstractServices

from purchase_order.models import PurchaseOrder, PurchaseOrderProducts


class PurchaseOrderServices(AbstractServices):


    model = PurchaseOrder


class PurchaseOrderProductsServices(AbstractServices):


    model = PurchaseOrderProducts

    def filter_by_purchase_order_id(order):
        return PurchaseOrderProducts.objects.filter(purchase_order=order)

