from user.models import User
from django.contrib.auth.hashers import make_password

class UserService:


    @staticmethod
    def query_all():
        return User.objects.all()
    
    @staticmethod
    def get(id):
        return User.objects.get(id=id)
    
    @staticmethod
    def create(name, last_name, email, password, user_type, document, phone):
        password = make_password(password)

        user = User.objects.create(
            name=name,
            last_name=last_name,
            email=email,
            password=password,
            user_type=user_type,
            document=document,
            phone=phone
        )

        return user

