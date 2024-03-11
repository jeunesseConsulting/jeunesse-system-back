from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    
    def ready(self):

        # Criando usuário admin se o mesmo não existir
        from user.services.user import UserService
        try:
            UserService.create(
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
