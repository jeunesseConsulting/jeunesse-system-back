from rest_framework import serializers

from user.models import User

from roles.serializer import RoleSerializer


class UserSerializer(serializers.ModelSerializer):


    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'password', 'name', 'last_name', 'email', 'person_type', 'document', 'phone', 'is_active', 'role']


class UserDetailSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    role = RoleSerializer()

    class Meta:
        model = User
        fields = ['id', 'password', 'name', 'last_name', 'email', 'person_type', 'document', 'phone', 'is_active', 'role']

