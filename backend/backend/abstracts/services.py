from django.db import models


class AbstractServices:


    model:models.Model

    @classmethod
    def query_all(cls):
        return cls.model.objects.all()
    
    @classmethod
    def get(cls, id):
        try:
            obj = cls.model.objects.get(id=id)
            return obj
        except cls.model.DoesNotExist:
            return None