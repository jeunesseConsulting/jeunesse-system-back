from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from payment_method.services.payment_method import PaymentMethodServices
from payment_method.serializer import PaymentMethodSerializer


class PaymentMethodView(AuthenticatedAPIView):


    model_serializer = PaymentMethodSerializer
    model_service = PaymentMethodServices


class PaymentMethodDetailView(AuthenticatedDetailAPIView):


    model_serializer = PaymentMethodSerializer
    model_service = PaymentMethodServices
