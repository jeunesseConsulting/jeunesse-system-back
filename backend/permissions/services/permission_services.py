from permissions.models import Permissions


class PermissionsServices:


    @staticmethod
    def query_all():
        return Permissions.objects.all()
    
    @staticmethod
    def get(id):
        try:
            permission = Permissions.objects.get(id=id)
            return permission
        except Permissions.DoesNotExist:
            return None

