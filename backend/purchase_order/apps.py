from django.apps import AppConfig
from django.db import connection


class PurchaseOrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'purchase_order'

    def ready(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM purchase_order_status;")
            record_count = cursor.fetchone()[0]

        if record_count < 4:
            from purchase_order.models import PurchaseOrderStatus

            status_list = [
                'Pendente',
                'Aprovada',
                'Cancelada',
                'Concluída'
            ]

            for obj in status_list:
                try:
                    PurchaseOrderStatus.objects.get_or_create(name=obj)
                except:
                    pass
