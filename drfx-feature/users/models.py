from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    # first_name = models.CharField()

    def __str__(self):
        return self.email
    

# class Userprofile(AbstractUser):
#     name = models.CharField(blank=True, max_length=255)
#     email = models.CharField(blank=True, max_length=255)
#     password = models.CharField(blank=True, max_length=255)

#     def __str__(self):
#         return self.email