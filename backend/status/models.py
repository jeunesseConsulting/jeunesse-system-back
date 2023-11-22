from django.db import models


class Status(models.Model):


    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'status'
