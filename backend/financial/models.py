from django.db import models

from user.models import User


class FinancialEntry(models.Model):


    responsible = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='financial_entry_responsible',
        blank=False,
        null=False
    )

    entry_type = models.CharField(max_length=1, null=False, blank=False)
    
    # Date to consider the financial entry
    entry_date = models.DateField(null=False, blank=False)

    # Date when the entry was made
    created_at = models.DateTimeField(auto_now_add=True)

    description = models.CharField(max_length=5000, null=True, blank=True)

    # FK of a service_order or a purchase_order, for manual entries this will be blank
    origin = models.IntegerField(null=True, blank=True)

    value = models.FloatField(null=False, blank=False)
