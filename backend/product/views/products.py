from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView
from rest_framework.response import Response
from rest_framework import status

from product.serializer import ProductSerializer, ProductCreateSerializer
from product.services.product import ProductServices


class ProductView(AuthenticatedAPIView):


    model_serializer = ProductSerializer
    model_service = ProductServices

    def get(self, request):
        products = self.model_service.query_all()
        type_filter = request.query_params.get('type')

        if type_filter:
            products = products.filter(type=type_filter)
        
        serializer = self.model_serializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ProductCreateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            product = self.model_service.get(serializer.instance.id)
            response_serializer = self.model_serializer(product)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ProductDetailView(AuthenticatedDetailAPIView):


    model_serializer = ProductSerializer
    model_service = ProductServices

    def put(self, request, id):
        product = self.model_service.get(id)
        data = request.data

        if product:
            serializer = ProductCreateSerializer(product, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                product = self.model_service.get(id)
                response_serializer = self.model_serializer(product)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)

