from backend.abstracts.views import AuthenticatedAPIView
from rest_framework.response import Response
from rest_framework import status

from roles.services.roles import RoleService
from roles.serializer import RoleSerializer


class RoleView(AuthenticatedAPIView):


    def get(self, _):
        roles = RoleService.query_all()
        serializer = RoleSerializer(roles, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = RoleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class RoleDetailView(AuthenticatedAPIView):


    def get(self, _, id):
        role = RoleService.get(id)

        if role:
            serializer = RoleSerializer(role)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        role = RoleService.get(id)
        data = request.data

        if role:
            serializer = RoleSerializer(role, data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id):
        role = RoleService.get(id)

        if role:
            role.delete()
            return Response(data={'message':'role deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
