from django.db import models

from product.models import Product


class PurchaseOrderProducts(models.Model):

    
    purchase_order = models.BigIntegerField(null=False, blank=False)

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='aux_product',
        null=False,
        blank=False
    )

    price = models.FloatField(null=False, blank=False)

    class Meta:
        db_table = 'aux_purchase_order_products'
