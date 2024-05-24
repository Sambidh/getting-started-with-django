from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User = get_user_model()

class User(AbstractUser):
    cellphone_number = models.CharField(max_length=15)

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

