from backend.abstracts.services import AbstractServices
from backend.exceptions import DataBaseException

from service.aux_models import OrderServices


class OrderServicesServices(AbstractServices):


    model = OrderServices

    def filter_by_service_order_id(order):
        try:
            return OrderServices.objects.filter(order=order)
        
        except Exception:
            raise DataBaseException
