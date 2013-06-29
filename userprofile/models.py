from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class SiteUser(AbstractUser):
    nickname = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True)
    phone = models.CharField(max_length=16)
    skype = models.CharField(max_length = 200)
    steam = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    cheif = models.BooleanField(null=False, default=False)
    position = models.CharField(max_length=200)
    objects = UserManager()

    def get_user():
        return self 
