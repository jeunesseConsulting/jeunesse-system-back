from django.db import models

from user.models import User


class Vehicle(models.Model):


    plate = models.CharField(max_length=7, null=False, blank=False)
    color = models.CharField(max_length=50, null=False, blank=False)
    brand = models.CharField(max_length=255, null=False, blank=False)
    model = models.CharField(max_length=255, null=False, blank=False)
    fabrication_year = models.CharField(max_length=4, null=False, blank=False)
    vehicle_type = models.CharField(db_column='type', max_length=255, null=False, blank=False)

    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='vehicle_owner',
        blank=False,
        null=False
    )

    def __str__(self):
        return self.plate
    
    class Meta:
        db_table = 'vehicles'
