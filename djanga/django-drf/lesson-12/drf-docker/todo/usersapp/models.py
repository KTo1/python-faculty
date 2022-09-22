from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ''' model for users  '''

    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=18)