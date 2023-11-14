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
from django.db.models import Sum

from service_order.utils import generate_service_order_pdf

from backend.settings import CLIENT_NAME

import datetime


class ServiceOrderView(AuthenticatedAPIView):

    
    model_serializer = ServiceOrderSerializer
    model_service = ServiceOrderServices

    def get(self, request):
        orders = ServiceOrderServices.query_all()
        status_filter = request.query_params.get('status')
        client_filter = request.query_params.get('client')

        if status_filter:
            orders = orders.filter(status__contains=status_filter)

        if client_filter:
            orders = orders.filter(client__name__icontains=client_filter)

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
            try:
                serializer = ServiceOrderSerializer(os)
                pdf = generate_service_order_pdf(serializer.data, CLIENT_NAME)
                return Response(data={
                    'service_order': int(id),
                    'pdf': pdf 
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={'error': e}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)


class ServiceOrderReportView(APIView):


    permission_classes = [IsAuthenticated]

    def post(self, request):
        orders = ServiceOrderServices.query_all()
        
        initial_date = request.data.get('initial_date')
        final_date = request.data.get('final_date')

        if not initial_date and not final_date:
            pass

        elif initial_date and not final_date:
            try:
                initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')
                initial_date = datetime.datetime.combine(initial_date.date(), datetime.time(0, 0, 0))
                final_date = datetime.datetime.now()
                orders = orders.filter(created_at__range=(initial_date, final_date))
            except Exception as e:
                return Response(data={
                    'messsage': 'invalid date parameter',
                    'error': str(e)
                })
            
        elif not initial_date and final_date:
            try:
                initial_date = datetime.datetime(1999, 1, 1, 0, 0, 0)
                final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d')
                final_date = datetime.datetime.combine(final_date.date(), datetime.time(23, 59, 59))
                orders = orders.filter(created_at__range=(initial_date, final_date))
            except Exception as e:
                return Response(data={
                    'messsage': 'invalid date parameter',
                    'error': str(e)
                })
            
        else:
            try:
                initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')
                initial_date = datetime.datetime.combine(initial_date.date(), datetime.time(0, 0, 0))
                final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d')
                final_date = datetime.datetime.combine(final_date.date(), datetime.time(23, 59, 59))
                orders = orders.filter(created_at__range=(initial_date, final_date))
            except Exception as e:
                return Response(data={
                    'messsage': 'invalid date parameter',
                    'error': str(e)
                })
            
        status_filter = request.query_params.get('status')
        if status_filter:
            ...


class ServiceOrderSummaryView(APIView):


    permission_classes = [IsAuthenticated]

    def post(self, request):
        orders = ServiceOrderServices.query_all()
        
        initial_date = request.data.get('initial_date')
        final_date = request.data.get('final_date')

        if not initial_date and not final_date:
            pass

        elif initial_date and not final_date:
            try:
                initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')
                initial_date = datetime.datetime.combine(initial_date.date(), datetime.time(0, 0, 0))
                final_date = datetime.datetime.now()
                orders = orders.filter(created_at__range=(initial_date, final_date))
            except Exception as e:
                return Response(data={
                    'messsage': 'invalid date parameter',
                    'error': str(e)
                })
            
        elif not initial_date and final_date:
            try:
                initial_date = datetime.datetime(1999, 1, 1, 0, 0, 0)
                final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d')
                final_date = datetime.datetime.combine(final_date.date(), datetime.time(23, 59, 59))
                orders = orders.filter(created_at__range=(initial_date, final_date))
            except Exception as e:
                return Response(data={
                    'messsage': 'invalid date parameter',
                    'error': str(e)
                })
            
        else:
            try:
                initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')
                initial_date = datetime.datetime.combine(initial_date.date(), datetime.time(0, 0, 0))
                final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d')
                final_date = datetime.datetime.combine(final_date.date(), datetime.time(23, 59, 59))
                orders = orders.filter(created_at__range=(initial_date, final_date))
            except Exception as e:
                return Response(data={
                    'messsage': 'invalid date parameter',
                    'error': str(e)
                })

        status_list = [
            'pendente',
            'aprovada',
            'andamento',
            'reprovada',
            'cancelada',
            'concluida'
        ]

        data = {}

        for status_value in status_list:
            data[status_value] = {}
            qty = orders.filter(status=status_value).count()
            total_services = orders.filter(status=status_value).aggregate(Sum('services_total_value'))
            total_products = orders.filter(status=status_value).aggregate(Sum('products_total_value'))

            if total_services['services_total_value__sum'] is None:
                total_services_value = 0.0
            else:
                total_services_value = total_services['services_total_value__sum']
            
            if total_products['products_total_value__sum'] is None:
                total_products_value = 0.0
            else:
                total_products_value = total_products['products_total_value__sum']

            data[status_value]['qty'] = qty
            data[status_value]['total_services'] = total_services_value
            data[status_value]['total_products'] = total_products_value

        return Response(data=data, status=status.HTTP_200_OK)




