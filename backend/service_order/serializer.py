from rest_framework import serializers

from service_order.models import ServiceOrder

from service.serializer import OrderServicesSerializer, OrderServicesDetailSerializer

from client.serializer import ClientSerializer
from vehicle.serializer import VehicleSerializer
from product.serializer import OrderProductsSerializer


class ServiceOrderCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = ServiceOrder
        fields = '__all__'


class ServiceOrderSerializer(serializers.ModelSerializer):


    services = serializers.SerializerMethodField()
    client = ClientSerializer()
    vehicle = VehicleSerializer()
    products = serializers.SerializerMethodField()

    class Meta:
        model = ServiceOrder
        fields = '__all__'

    def get_services(self, obj):
        if obj.services.exists():
            return OrderServicesDetailSerializer(obj.services, many=True).data
        else:
            return []
        
    def get_products(self, obj):
        if obj.products.exists():
            return OrderProductsSerializer(obj.products, many=True).data
        else:
            return []

        