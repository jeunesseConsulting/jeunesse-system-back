from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from product.serializer import ProductMeasureUnitSerializer
from product.services.measure_unit import ProductMeasureUnitServices


class ProductMeasureUnitView(AuthenticatedAPIView):

    
    model_serializer = ProductMeasureUnitSerializer
    model_service = ProductMeasureUnitServices


class ProductMeasureUnitDetailView(AuthenticatedDetailAPIView):


    model_serializer = ProductMeasureUnitSerializer
    model_service = ProductMeasureUnitServices
