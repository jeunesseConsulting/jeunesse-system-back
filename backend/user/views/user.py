from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView
from backend.exceptions import DataBaseException

from rest_framework.response import Response
from rest_framework import status

from user.services.user import UserService
from user.serializer import UserSerializer, UserDetailSerializer

from django.contrib.auth.hashers import make_password


class UserView(AuthenticatedAPIView):

    
    def get(self, request):
        try:
            users = UserService.query_all()
            active_filter = request.query_params.get('is_active')

            active_map = {
                'true': True,
                'false': False
            }

            if active_filter in active_map:
                users = users.filter(is_active=active_map[active_filter])

            serializer = UserDetailSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                user = UserService.create(**serializer.validated_data)
                response_serializer = UserDetailSerializer(user)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)



class UserDetailView(AuthenticatedDetailAPIView):


    model_serializer = UserSerializer
    model_service = UserService
        
    def put(self, request, id):
        try:
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

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

