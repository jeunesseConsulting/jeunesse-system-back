from django.db import models
from backend.exceptions import DataBaseException


class AbstractServices:


    model:models.Model

    @classmethod
    def query_all(cls):
        try:
            return cls.model.objects.all()
        
        except:
            raise DataBaseException
    
    @classmethod
    def get(cls, id):
        try:
            obj = cls.model.objects.get(id=id)
            return obj
        
        except cls.model.DoesNotExist:
            return None
        
        except Exception:
            raise DataBaseException