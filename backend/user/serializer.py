from rest_framework import serializers

from user.models import User

from roles.serializer import RoleSerializer
from permissions.serializer import PermissionsSerializer


class UserSerializer(serializers.ModelSerializer):


    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'password', 'name', 'last_name', 'email', 'person_type', 'document', 'phone', 'is_active', 'role', 'permissions']


class UserDetailSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    role = RoleSerializer()
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'password', 'name', 'last_name', 'email', 'person_type', 'document', 'phone', 'is_active', 'role', 'permissions']

    def get_permissions(self, obj):
        if obj.permissions.exists():
            return PermissionsSerializer(obj.permissions.all(), many=True).data
        else:
            return None

