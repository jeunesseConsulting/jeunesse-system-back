from django.db import models

from product.models import Product


class OrderProducts(models.Model):


    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='product_aux',
        null=False,
        blank=False
    )

    order = models.BigIntegerField()

    quantity = models.FloatField(default=0.0)

    class Meta:
        db_table = 'aux_order_products'
