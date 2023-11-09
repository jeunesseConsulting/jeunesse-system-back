from backend.abstracts.services import AbstractServices

from service.aux_models import OrderServices


class OrderServicesServices(AbstractServices):


    model = OrderServices

    def filter_by_service_order_id(order):
        return OrderServices.objects.filter(order=order)

