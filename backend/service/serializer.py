from rest_framework import serializers

from service.models import Service
from service.aux_models import OrderServices


class ServiceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Service
        fields = '__all__'


class OrderServicesSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderServices
        fields = '__all__'


class OrderServicesDetailSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()

    class Meta:
        model = OrderServices
        fields = '__all__'
