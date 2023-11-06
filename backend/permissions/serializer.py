from rest_framework import serializers

from permissions.models import Permissions


class PermissionsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Permissions
        fields = '__all__'

