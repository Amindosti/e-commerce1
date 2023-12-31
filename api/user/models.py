from django.db import models
from django.contrib.auth.models import AbstractUser

choices = [
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('PFR', 'prefer not to say'),
]

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=choices, default='PFR')

    session_token = models.CharField(max_length=10, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name