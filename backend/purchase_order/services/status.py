from backend.abstracts.services import AbstractServices

from purchase_order.models import PurchaseOrderStatus


class PurchaseOrderStatusServices(AbstractServices):


    model = PurchaseOrderStatus
