from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from accounts.maneger import WaiterManager


class Waiter(AbstractBaseUser):
    """Waiter model with custom authentication."""

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)  # Password will be hashed

    objects = WaiterManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
