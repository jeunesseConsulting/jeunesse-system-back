from django.db import models


class Client(models.Model):


    client_type = models.CharField(max_length=1, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    document = models.CharField(max_length=20)
    address = models.CharField(max_length=510)
    zip_code = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'clients'
