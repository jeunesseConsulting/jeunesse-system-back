from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from service.services.service import ServiceServices
from service.serializer import ServiceSerializer


class ServiceView(AuthenticatedAPIView):


    model_serializer = ServiceSerializer
    model_service = ServiceServices


class ServiceDetailView(AuthenticatedDetailAPIView):


    model_serializer = ServiceSerializer
    model_service = ServiceServices
