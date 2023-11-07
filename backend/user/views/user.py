from backend.abstracts.views import AuthenticatedAPIView
from rest_framework.response import Response
from rest_framework import status

from user.services.user import UserService
from user.serializer import UserSerializer, UserDetailSerializer

from django.contrib.auth.hashers import make_password


class UserView(AuthenticatedAPIView):

    
    def get(self, request):
        users = UserService.query_all()
        serializer = UserDetailSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            user = UserService.create(**serializer.validated_data)
            response_serializer = UserDetailSerializer(user)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(AuthenticatedAPIView):


    def get(self, request, id):
        user = UserService.get(id)

        if user:
            serializer = UserDetailSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        user = UserService.get(id)
        
        try:
            password = request.data.get('password')
        except:
            pass

        if password:
            request.data['password'] = make_password(password)

        if user:
            serializer = UserSerializer(user, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response_serializer = UserDetailSerializer(user)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id):
        user = UserService.get(id)

        if user:
            user.delete()
            return Response(data={'message':'user deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)

