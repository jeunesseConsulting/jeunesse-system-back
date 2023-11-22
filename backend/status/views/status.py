from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from status.serializer import StatusSerializer
from status.services.status import StatusServices


class StatusView(AuthenticatedAPIView):


    model_serializer = StatusSerializer
    model_service = StatusServices


class StatusDetailView(AuthenticatedDetailAPIView):


    model_serializer = StatusSerializer
    model_service = StatusServices

