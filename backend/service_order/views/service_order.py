from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from service_order.serializer import ServiceOrderSerializer, ServiceOrderCreateSerializer, ServiceOrderDetailSerializer
from service_order.services.service_order import ServiceOrderServices

from service.serializer import OrderServicesSerializer
from service.services.order_services import OrderServicesServices

from rest_framework.response import Response
from rest_framework import status

from django.db import transaction


class ServiceOrderView(AuthenticatedAPIView):

    
    model_serializer = ServiceOrderSerializer
    model_service = ServiceOrderServices

    @transaction.atomic
    def post(self, request):
        data = request.data
        services_data = data.pop('services', [])
        order_data = data.copy()
        serializer = ServiceOrderCreateSerializer(data=order_data)

        if serializer.is_valid():
            order_instance = serializer.save()
            for service in services_data:
                service_serializer = OrderServicesSerializer(data={
                    'service': service['service'],
                    'order': order_instance.id,
                    'price': service['price']
                })
                if service_serializer.is_valid():
                    service_serializer.save()
                else:
                    return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            order_instance.services.set(OrderServicesServices.filter_by_service_order_id(order_instance.id))
            response_serializer = ServiceOrderDetailSerializer(ServiceOrderServices.get(order_instance.id))
            print(response_serializer.data)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceOrderDetailView(AuthenticatedDetailAPIView):


    model_serializer = ServiceOrderSerializer
    model_service = ServiceOrderServices

