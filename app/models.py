from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/',blank=True)
    address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)



    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Patient(CustomUser):
    
    def __str__(self):
        return self.username

class Doctor(CustomUser):
    pass
