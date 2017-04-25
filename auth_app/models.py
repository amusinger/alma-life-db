from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=128, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'