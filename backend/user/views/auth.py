from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from user.services.user import UserService

from backend.exceptions import DataBaseException


class AuthorizationTokenView(APIView):


    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
        
            user = UserService.auth(email, password)
        
            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response(data={'token':access_token, 'user_id':user.id}, status=status.HTTP_200_OK)

            return Response(data={'message':'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
