from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    
    def ready(self):

        # Creating admin user on first initialization
        from user.services.user import UserService
        from permissions.models import Permissions

        user = None

        try:
            user = UserService.create(
                name='admin',
                last_name='admin',
                email='admin@admin.com',
                password='admin@123',
                person_type='P',
                document='123',
                phone='123',
            )
        except:
            pass

        # Creating permissions on first initialization
        from permissions.models import Permissions

        permissions_list = [
            'DASHBOARDS',
            'FINANCEIRO',
            'REGISTERS',
            'USERS',
            'CLIENTS',
            'ROLES',
            'PERMISSIONS',
            'PRODUCTS',
            'SERVICES',
            'PRODUCTS_TYPE',
            'MEASURES_TYPES',
            'VEHICLES',
            'SUPPLIERS',
            'OS',
            'OC',
            'QUICK_BUDGET',
            'SCHEDULER',
            'HISTORIC',
            'HISTORIC_CLIENTS',
        ]

        for permission in permissions_list:
            try:
                Permissions.objects.create(
                    name=permission
                )
                    
            except:
                pass

        # Setting all permissions for admin user
        permissions = Permissions.objects.values_list('id', flat=True)

        if user:
            user.permissions.set(permissions)

        
