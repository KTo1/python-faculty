from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ''' model for users  '''

    image = models.ImageField(upload_to='users_images', blank=True)
    age = models.PositiveIntegerField(default=18)

