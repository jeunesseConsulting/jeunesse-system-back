from django.db import models

from service.models import Service

class OrderServices(models.Model):


    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name='service_aux',
        null=False,
        blank=False
    )

    order = models.BigIntegerField()

    price = models.FloatField(default=0.0)

    class Meta:
        db_table = 'aux_order_services'


