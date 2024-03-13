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
            'CLIENTS',
            'PAYMENT_METHODS',
            'PERMISSIONS',
            'PRODUCTS',
            'PURCHASE_ORDERS',
            'ROLES',
            'SERVICES',
            'SERVICE_ORDERS',
            'SUPPLIERS',
            'USERS',
            'VEHICLES',
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

        
