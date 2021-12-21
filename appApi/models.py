from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True, max_length=200)
    phone = models.CharField(max_length=200, null=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email