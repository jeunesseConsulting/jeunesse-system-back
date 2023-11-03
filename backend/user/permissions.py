from rest_framework import permissions

from rest_framework_simplejwt.tokens import RefreshToken

from user.services.user_services import UserService


class IsUserAuthenticated(permissions.BasePermission):
    

    def has_permission(self, request, view):
        email = request.data.get('email')
        password = request.data.get('password')

        user = UserService.auth(email, password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            request.access_token = access_token

            return True
        
        else:
            return False

