from django.db import models


class PaymentMethod(models.Model):


    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'payment_method'
