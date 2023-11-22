from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class StatusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'status'

    def ready(self):
        @receiver(post_migrate)
        def populate_status_table(sender, **kwargs):
            from status.models import Status

            status_list = [
                'Pendente',
                'Aprovada',
                'Andamento',
                'Reprovada',
                'Cancelada',
                'Concluída'
            ]

            Status.objects.all().delete()

            for obj in status_list:
                try:
                    Status.objects.create(name=obj)
                except:
                    pass

