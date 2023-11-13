from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from service_order.serializer import ServiceOrderSerializer, ServiceOrderCreateSerializer
from service_order.services.service_order import ServiceOrderServices

from service.serializer import OrderServicesSerializer
from service.services.order_services import OrderServicesServices

from product.serializer import OrderProductsCreateSerializer
from product.services.order_products import OrderProductsServices

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.db import transaction

from service_order.utils import generate_service_order_pdf

from backend.settings import CLIENT_NAME


class ServiceOrderView(AuthenticatedAPIView):

    
    model_serializer = ServiceOrderSerializer
    model_service = ServiceOrderServices

    def get(self, request):
        orders = ServiceOrderServices.query_all()
        serializer = self.model_serializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    @transaction.atomic
    def post(self, request):
        data = request.data
        services_data = data.pop('services', [])
        products_data = data.pop('products', [])
        order_data = data.copy()
        serializer = ServiceOrderCreateSerializer(data=order_data)

        if serializer.is_valid():
            order_instance = serializer.save()

            for service in services_data:
                service_serializer = OrderServicesSerializer(data={
                    'service': service['id'],
                    'order': order_instance.id,
                    'price': service['price']
                })
                if service_serializer.is_valid():
                    service_serializer.save()
                else:
                    return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            for product in products_data:
                product_serializer = OrderProductsCreateSerializer(data={
                    'product': product['id'],
                    'order': order_instance.id,
                    'quantity': product['quantity']
                })
                if product_serializer.is_valid():
                    product_serializer.save()
                else:
                    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            order_instance.products.set(OrderProductsServices.filter_by_service_order_id(order_instance.id))
            order_instance.services.set(OrderServicesServices.filter_by_service_order_id(order_instance.id))
            response_serializer = self.model_serializer(ServiceOrderServices.get(order_instance.id))
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceOrderDetailView(AuthenticatedDetailAPIView):


    model_serializer = ServiceOrderSerializer
    model_service = ServiceOrderServices

    def put(self, request, id):
        data = request.data
        services_data = data.pop('services', [])
        products_data = data.pop('products', [])
        order_data = data.copy()
        order = self.model_service.get(id)

        if order:

            #Setando os serviços novos
            if services_data:
                services = OrderServicesServices.filter_by_service_order_id(order.id)
                for old_service in services:
                    old_service.delete()

                for service in services_data:
                    service_serializer = OrderServicesSerializer(data={
                        'service': service['id'],
                        'order': order.id,
                        'price': service['price']
                    })
                    if service_serializer.is_valid():
                        service_serializer.save()
                    else:
                        return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                order.services.set(OrderServicesServices.filter_by_service_order_id(order.id))

            
            #Setando os produtos novos
            if products_data:
                products = OrderProductsServices.filter_by_service_order_id(order.id)
                for old_products in products:
                    old_products.delete()

                for product in products_data:
                    product_serializer = OrderProductsCreateSerializer(data={
                        'product': product['id'],
                        'order': order.id,
                        'quantity': product['quantity']
                    })
                    if product_serializer.is_valid():
                        product_serializer.save()
                    else:
                        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                order.products.set(OrderProductsServices.filter_by_service_order_id(order.id))


            #Setando o resto dos campos
            if order_data:
                serializer = ServiceOrderCreateSerializer(order, data=order_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            response_serializer = self.model_serializer(ServiceOrderServices.get(order.id))
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        

class ServiceOrderPDFView(APIView):


    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        os = ServiceOrderServices.get(id)

        if os:
            serializer = ServiceOrderSerializer(os)
            pdf = generate_service_order_pdf(serializer.data, CLIENT_NAME)
            return Response(data={
                'service_order': int(id),
                'pdf': pdf 
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
