from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=150, unique=True) 
    birthday = models.DateField()  
    gender = models.CharField(max_length=10, blank=True, null=True) 
    introduction = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True) 

    # REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'nickname', 'birthday']
