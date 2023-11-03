from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=510, null=False, blank=False)
    person_type = models.CharField(max_length=1, null=False, blank=False, default='P')
    document = models.CharField(max_length=20, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'

