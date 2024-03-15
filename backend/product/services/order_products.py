from backend.abstracts.services import AbstractServices
from backend.exceptions import DataBaseException

from product.aux_models import OrderProducts


class OrderProductsServices(AbstractServices):


    model = OrderProducts

    def filter_by_service_order_id(order):
        try:
            products = OrderProducts.objects.filter(order=order)
            return products
        
        except Exception:
            raise DataBaseException
