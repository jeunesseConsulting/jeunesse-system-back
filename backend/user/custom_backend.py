from django.contrib.auth.backends import BaseBackend
from user.models import User

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        email = email.lower()
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
