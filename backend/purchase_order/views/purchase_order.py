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

                try:
                    quantity = product['quantity']
                except:
                    quantity = 0.0

                product_serializer = PurchaseOrderProductsCreateSerializer(data={
                    'purchase_order': None,
                    'product': id,
                    'price': price,
                    'quantity': quantity
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

    @transaction.atomic
    def put(self, request, id):
        data = request.data
        products_data = data.pop('products', [])
        order_data = data.copy()

        order = PurchaseOrderServices.get(id)
        
        if data:
            if order:
                if order_data:
                    serializer = PurchaseOrderCreateSerializer(instance=order, data=order_data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    pass
                
                if products_data:
                    old_products = PurchaseOrderProductsServices.filter_by_purchase_order_id(order.id)

                    product_serializers = []
                    for product in products_data:
                        try:
                            price = product['price']
                        except:
                            price = 0.0 

                        try:
                            quantity = product['quantity']
                        except:
                            quantity = 0.0

                        try:
                            id = product['id']
                        except:
                            return Response(data={'message':'missing product id'}, status=status.HTTP_400_BAD_REQUEST)

                        new_product_serializer = PurchaseOrderProductsCreateSerializer(data={
                            'purchase_order': order.id,
                            'product': product['id'],
                            'price': price,
                            'quantity': quantity
                        })

                        if new_product_serializer.is_valid():
                            product_serializers.append(new_product_serializer)
                        else:
                            return Response(new_product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                    if old_products:
                        for product in old_products:
                            product.delete()

                    for product_serializer in product_serializers:
                        product_serializer.save()

                    order.products.set(PurchaseOrderProductsServices.filter_by_purchase_order_id(order.id))
                    response_serializer = PurchaseOrderSerializer(PurchaseOrderServices.get(order.id))
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                else:
                    response_serializer = PurchaseOrderSerializer(PurchaseOrderServices.get(order.id))
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data={'message':'missing data'}, status=status.HTTP_400_BAD_REQUEST)

