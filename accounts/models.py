from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('free', 'Free'),
        ('member', 'Member'),
    ]    

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='free')

    def __str__(self):
        return self.username
    