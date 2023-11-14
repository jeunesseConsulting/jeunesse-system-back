from rest_framework import serializers

from vehicle.models import Vehicle

from client.serializer import ClientSerializer


class VehicleCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):


    owner = ClientSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleOrderViewSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Vehicle
        fields = [
            'plate',
            'color',
            'brand',
            'model',
            'fabrication_year',
            'type'
        ]
