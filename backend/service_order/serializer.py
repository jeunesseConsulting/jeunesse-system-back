from rest_framework import serializers

from service_order.models import ServiceOrder

from service.serializer import OrderServicesSerializer, OrderServicesDetailSerializer


class ServiceOrderCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = ServiceOrder
        fields = '__all__'


class ServiceOrderSerializer(serializers.ModelSerializer):


    services = serializers.SerializerMethodField()

    class Meta:
        model = ServiceOrder
        fields = '__all__'

    def get_services(self, obj):
        if obj.services.exists():
            return OrderServicesSerializer(obj.services.all(), many=True).data
        else:
            return []
        

class ServiceOrderDetailSerializer(serializers.ModelSerializer):


    services = serializers.SerializerMethodField()

    class Meta:
        model = ServiceOrder
        fields = '__all__'

    def get_services(self, obj):
        if obj.services.exists():
            return OrderServicesDetailSerializer(obj.services, many=True).data
        else:
            return []
