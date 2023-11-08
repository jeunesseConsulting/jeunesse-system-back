from rest_framework import serializers

from vehicle.models import Vehicle

from user.serializer import UserDetailSerializer


class VehicleCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):


    owner = UserDetailSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'
