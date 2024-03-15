from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView
from backend.exceptions import DataBaseException

from rest_framework.response import Response
from rest_framework import status

from product.serializer import ProductSerializer, ProductCreateSerializer
from product.services.product import ProductServices


class ProductView(AuthenticatedAPIView):


    model_serializer = ProductSerializer
    model_service = ProductServices

    def get(self, request):
        try:
            products = self.model_service.query_all()
            type_filter = request.query_params.get('type')

            if type_filter:
                products = products.filter(type=type_filter)
            
            serializer = self.model_serializer(products, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def post(self, request):
        try:
            data = request.data
            serializer = ProductCreateSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                product = self.model_service.get(serializer.instance.id)
                response_serializer = self.model_serializer(product)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


class ProductDetailView(AuthenticatedDetailAPIView):


    model_serializer = ProductSerializer
    model_service = ProductServices

    def put(self, request, id):
        try:
            product = self.model_service.get(id)
            data = request.data

            if product:
                serializer = ProductCreateSerializer(product, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    product = self.model_service.get(id)
                    response_serializer = self.model_serializer(product)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

