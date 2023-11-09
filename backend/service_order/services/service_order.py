from backend.abstracts.services import AbstractServices

from service_order.models import ServiceOrder


class ServiceOrderServices(AbstractServices):

    model = ServiceOrder


