from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return f'{self.username}'
