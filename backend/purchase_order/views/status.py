from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from purchase_order.serializer import PurchaseOrderStatusSerializer
from purchase_order.services.status import PurchaseOrderStatusServices


class PurchaseOrderStatusView(AuthenticatedAPIView):


    model_serializer = PurchaseOrderStatusSerializer
    model_service = PurchaseOrderStatusServices


class PurchaseOrderStatusDetailView(AuthenticatedDetailAPIView):


    model_serializer = PurchaseOrderStatusSerializer
    model_service = PurchaseOrderStatusServices

