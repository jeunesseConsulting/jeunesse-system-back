from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from purchase_order.serializer import PurchaseOrderSerializer, PurchaseOrderCreateSerializer, PurchaseOrderProductsCreateSerializer
from purchase_order.services.purchase_order import PurchaseOrderServices, PurchaseOrderProductsServices

from product.services.product import ProductServices
from product.serializer import ProductCreateSerializer

from django.db import transaction

from rest_framework.response import Response
from rest_framework import status


class PurchaseOrderView(AuthenticatedAPIView):


    model_serializer = PurchaseOrderSerializer
    model_service = PurchaseOrderServices

    @transaction.atomic
    def post(self, request):
        data = request.data
        products_data = data.pop('products', [])
        order_data = data.copy()

        serializer = PurchaseOrderCreateSerializer(data=order_data)
        
        if serializer.is_valid():

            product_serializers = []
            for product in products_data:
                try:
                    id = product['id']
                except:
                    new_product_serializer = ProductCreateSerializer(data={'name':product['name']})
                    if new_product_serializer.is_valid():
                        new_product_instance = new_product_serializer.save()
                        id = new_product_instance.id
                    else:
                        return Response(new_product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                try:
                    price = product['price']
                except:
                    price = 0.0

                product_serializer = PurchaseOrderProductsCreateSerializer(data={
                    'purchase_order': None,
                    'product': id,
                    'price': price,
                    'quantity': product['quantity']
                })
                
                if product_serializer.is_valid():
                    product_serializers.append(product_serializer)
                else:
                    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            order_instance = serializer.save()
            for product_serializer in product_serializers:
                product_serializer.validated_data['purchase_order'] = order_instance.id
                product_serializer.save()

                
            order_instance.products.set(PurchaseOrderProductsServices.filter_by_purchase_order_id(order_instance.id))
            response_serializer = PurchaseOrderSerializer(PurchaseOrderServices.get(order_instance.id))
            return Response(response_serializer.data, status=status.HTTP_200_OK)


        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class PurchaseOrderDetailView(AuthenticatedDetailAPIView):


    model_serializer = PurchaseOrderSerializer
    model_service = PurchaseOrderServices



