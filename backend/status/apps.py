from django.apps import AppConfig
from django.db import connection


class StatusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'status'

    def ready(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM status;")
            record_count = cursor.fetchone()[0]

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

