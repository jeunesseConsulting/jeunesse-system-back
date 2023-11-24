from django.db import models

from product.models import Product


class PurchaseOrderProducts(models.Model):

    
    purchase_order = models.BigIntegerField(null=True, blank=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='aux_product',
        null=False,
        blank=False
    )

    price = models.FloatField(null=False, blank=False)
    quantity = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'aux_purchase_order_products'
