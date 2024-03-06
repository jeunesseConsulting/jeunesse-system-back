from django.apps import AppConfig
from django.db import connection


class StatusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'status'

    def ready(self):
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT COUNT(*) FROM status;")
                record_count = cursor.fetchone()[0]
            except:
                record_count = 100
                pass

        if record_count < 7:
            from status.models import Status

            status_list = [
                'Pendente',
                'Aprovada',
                'Andamento',
                'Reprovada',
                'Cancelada',
                'Concluída',
                'Pendente Retirada',
            ]

            for obj in status_list:
                try:
                    Status.objects.get_or_create(name=obj)
                except:
                    pass

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
                phone='123'
            )
        except:
            pass

