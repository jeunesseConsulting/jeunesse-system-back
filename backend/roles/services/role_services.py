from roles.models import Role


class RoleService:


    @staticmethod
    def query_all():
        return Role.objects.all()
    
    @staticmethod
    def get(id):
        try:
            role = Role.objects.get(id=id)
            return role
        except Role.DoesNotExist:
            return None
    
