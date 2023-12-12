from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from service_order.serializer import ServiceOrderSerializer, ServiceOrderCreateSerializer
from service_order.services.service_order import ServiceOrderServices

from service.serializer import OrderServicesSerializer, ServiceSerializer
from service.services.order_services import OrderServicesServices

from product.serializer import OrderProductsCreateSerializer
from product.services.order_products import OrderProductsServices
from product.services.product import ProductServices

from status.services.status import StatusServices

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.db import transaction
from django.db.models import Sum

from service_order.utils import generate_service_order_pdf, SendNotification

from backend.settings import CLIENT_NAME

import datetime
import asyncio
import schedule


class ServiceOrderView(AuthenticatedAPIView):

    
    model_serializer = ServiceOrderSerializer
    model_service = ServiceOrderServices

    def get(self, request):
        orders = ServiceOrderServices.query_all()
        status_filter = request.query_params.get('status')
        client_filter = request.query_params.get('client')
        client_id_filter = request.query_params.get('client_id')

        if status_filter:
            orders = orders.filter(status=status_filter)

        if client_filter and not client_id_filter:
            orders = orders.filter(client__name__icontains=client_filter)

        if client_id_filter:
            orders = orders.filter(client=client_id_filter)

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
                try:
                    id = service['id']
                except:
                    new_service_serializer = ServiceSerializer(data={
                        'name': service['name'],
                        'standard_value': service['price']
                    })
                    if new_service_serializer.is_valid():
                        new_service_serializer.save()
                        service_instance = new_service_serializer.instance
                        id = service_instance.id
                    else:
                        return Response(new_service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                service_serializer = OrderServicesSerializer(data={
                    'service': id,
                    'order': order_instance.id,
                    'price': service['price']
                })
                if service_serializer.is_valid():
                    service_serializer.save()
                else:
                    return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            for product in products_data:
                try:
                    id = product['id']
                except:
                    return Response(data={'message': 'missing product id'})
                
                try:
                    quantity = product['quantity']
                except:
                    quantity = 0.0

                product_serializer = OrderProductsCreateSerializer(data={
                    'product': id,
                    'order': order_instance.id,
                    'quantity': quantity
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

        if order.status.name == 'Concluída': 
            return Response(data={'message':'service order closed'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if order:

            #Setando os serviços novos
            if services_data:
                services = OrderServicesServices.filter_by_service_order_id(order.id)
                for old_service in services:
                    old_service.delete()

                for service in services_data:
                    try:
                        id = service['id']
                    except:
                        new_service_serializer = ServiceSerializer(data={
                            'name': service['name'],
                            'standard_value': service['price']
                        })
                        if new_service_serializer.is_valid():
                            new_service_serializer.save()
                            service_instance = new_service_serializer.instance
                            id = service_instance.id
                        else:
                            return Response(new_service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                    service_serializer = OrderServicesSerializer(data={
                        'service': id,
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
                    status_os = StatusServices.get(serializer.validated_data['status'].id)
                    if status_os.name == 'Concluída':
                        for product_aux in order.products.all():
                            product = ProductServices.get(product_aux.product.id)
                            old_qty = product.quantity
                            product.quantity -= product_aux.quantity
                            if product.quantity < 0:
                                return Response(data={
                                    'message':'insufficient quantity in stock',
                                    'product_id': product.id,
                                    'stock_qty': old_qty,
                                    'os_qty': product_aux.quantity
                                })
                            else:
                                product.save()
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            new_order = ServiceOrderServices.get(order.id)
            response_serializer = self.model_serializer(new_order)

            if new_order.status.name == 'Concluída':
                schedule.every(1).seconds.do(lambda: asyncio.run(SendNotification.send_finished_order_notification(order.id)))

            if new_order.status.name == 'Cancelada':
                schedule.every(1).seconds.do(lambda: asyncio.run(SendNotification.send_canceled_order_notification(order.id)))

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
            orders = orders.filter(status__contains=status_filter)

        client_filter = request.query_params.get('client')
        if client_filter:
            orders = orders.filter(client__name__icontains=client_filter)

        vehicle_filter = request.query_params.get('vehicle')
        if vehicle_filter:
            orders = orders.filter(vehicle__model__icontains=vehicle_filter)

        serializer = ServiceOrderSerializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


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

        status_list = StatusServices.query_all()

        data = {}

        for status_instance in status_list:
            data[status_instance.name] = {}
            qty = orders.filter(status=status_instance.id).count()
            total_services = orders.filter(status=status_instance.id).aggregate(Sum('services_total_value'))
            total_products = orders.filter(status=status_instance.id).aggregate(Sum('products_total_value'))

            if total_services['services_total_value__sum'] is None:
                total_services_value = 0.0
            else:
                total_services_value = total_services['services_total_value__sum']
            
            if total_products['products_total_value__sum'] is None:
                total_products_value = 0.0
            else:
                total_products_value = total_products['products_total_value__sum']

            data[status_instance.name]['qty'] = qty
            data[status_instance.name]['total_services'] = total_services_value
            data[status_instance.name]['total_products'] = total_products_value

        return Response(data=data, status=status.HTTP_200_OK)

