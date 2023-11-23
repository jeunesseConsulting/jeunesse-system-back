from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from supplier.services.supplier import SupplierServices
from supplier.serializer import SupplierSerializer


class SupplierView(AuthenticatedAPIView):


    model_serializer = SupplierSerializer
    model_service = SupplierServices


class SupplierDetailView(AuthenticatedDetailAPIView):


    model_serializer = SupplierSerializer
    model_service = SupplierServices
