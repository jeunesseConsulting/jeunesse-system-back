from backend.abstracts.services import AbstractServices

from payment_method.models import PaymentMethod


class PaymentMethodServices(AbstractServices):

    
    model = PaymentMethod

