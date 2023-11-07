from backend.abstracts.views import AuthenticatedAPIView
from rest_framework.response import Response
from rest_framework import status

from permissions.services.permission import PermissionsServices
from permissions.serializer import PermissionsSerializer


class PermissionsView(AuthenticatedAPIView):


    def get(self, request):
        permissions = PermissionsServices.query_all()
        serializer = PermissionsSerializer(permissions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = PermissionsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PermissionsDetailView(AuthenticatedAPIView):


    def get(self, request, id):
        permission = PermissionsServices.get(id)

        if permission:
            serializer = PermissionsSerializer(permission)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        permission = PermissionsServices.get(id)
        data = request.data

        if permission:
            serializer = PermissionsSerializer(permission, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id):
        permission = PermissionsServices.get(id)

        if permission:
            permission.delete()
            return Response(data={'message':'permission deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)

