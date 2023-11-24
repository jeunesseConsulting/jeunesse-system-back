from django.db import models

from purchase_order.aux_models import PurchaseOrderProducts

from supplier.models import Supplier


class PurchaseOrderStatus(models.Model):


    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'purchase_order_status'


class PurchaseOrder(models.Model):


    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name='po_supplier',
        null=True,
        blank=True
    )

    status = models.ForeignKey(
        PurchaseOrderStatus,
        on_delete=models.PROTECT,
        related_name='po_status',
        null=True,
        blank=True
    )

    products = models.ManyToManyField(
        PurchaseOrderProducts,
        related_name='po_products',
        blank=True
    )

    delivery_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=510, blank=True, null=True)
    created_at = models.DateTimeField(auto_created=True, blank=True, null=True)

    class Meta:
        db_table = 'purchase_order'
