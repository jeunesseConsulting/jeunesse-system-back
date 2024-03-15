from user.models import User
from django.contrib.auth.hashers import make_password, check_password

from backend.exceptions import DataBaseException
from backend.abstracts.services import AbstractServices

class UserService(AbstractServices):


    model = User
    
    @staticmethod
    def create(name, last_name, email, password, person_type, document, phone, role=None, permissions=None, gender=None, birth_date=None):
        try:
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
                gender=gender,
                birth_date=birth_date
            )

            if permissions:
                user.permissions.set(permissions)

            return user
        
        except Exception:
            raise DataBaseException
    
    @staticmethod
    def auth(email, password):
        try:
            user = User.objects.get(email=email)
            
        except User.DoesNotExist:
            return None
        
        except Exception:
            raise DataBaseException
        
        if check_password(password, user.password):
            return user

        return None


