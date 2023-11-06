from user.models import User
from django.contrib.auth.hashers import make_password, check_password

class UserService:


    @staticmethod
    def query_all():
        return User.objects.all()
    
    @staticmethod
    def get(id):
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            return None
    
    @staticmethod
    def create(name, last_name, email, password, person_type, document, phone, role=None, permissions=None):
        password = make_password(password)

        user = User.objects.create(
            name=name,
            last_name=last_name,
            email=email,
            password=password,
            person_type=person_type,
            document=document,
            phone=phone,
            role=role,
        )

        if permissions:
            user.permissions.set(permissions)

        return user
    
    @staticmethod
    def auth(email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        
        if check_password(password, user.password):
            return user
        else:
            return None


