from django.db import models


class Service(models.Model):


    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    standard_value = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'services'

