from django.db import models

from client.models import Client
from vehicle.models import Vehicle
from service.aux_models import OrderServices
from product.aux_models import OrderProducts


class ServiceOrder(models.Model):


    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='os_client',
        null=False,
        blank=False
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='os_vehicle',
        null=False,
        blank=False
    )

    comments = models.CharField(max_length=1000, null=True, blank=True)

    services = models.ManyToManyField(
        OrderServices,
        related_name='os_services',
        blank=True
    )

    products = models.ManyToManyField(
        OrderProducts,
        related_name='os_products',
        blank=True
    )

    services_total_value = models.FloatField(default=0.0)
    products_total_value = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'service_order'

