from django.db import models


class Role(models.Model):

    role = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.role
    
    class Meta:
        db_table = 'roles'
