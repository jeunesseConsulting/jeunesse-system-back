from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):


    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'password', 'name', 'last_name', 'email', 'person_type', 'document', 'phone', 'is_active']

