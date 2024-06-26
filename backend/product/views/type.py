from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from product.serializer import ProductTypeSerializer
from product.services.type import ProductTypeServices


class ProductTypeView(AuthenticatedAPIView):


    model_serializer = ProductTypeSerializer
    model_service = ProductTypeServices

class ProductTypeDetailView(AuthenticatedDetailAPIView):


    model_serializer = ProductTypeSerializer
    model_service = ProductTypeServices

