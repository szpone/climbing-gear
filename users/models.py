from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Climber(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.username
