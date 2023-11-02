from django.db import models

class User(models.Model):


    name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=510, null=False, blank=False)
    user_type = models.CharField(max_length=1, null=False, blank=False)
    document = models.CharField(max_length=20, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'

