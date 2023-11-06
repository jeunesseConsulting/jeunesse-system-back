from django.db import models


class Permissions(models.Model):


    permission = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.permission
    
    class Meta:
        db_table = 'permissions'
