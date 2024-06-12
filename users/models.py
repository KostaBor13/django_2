from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
    )
    phone = models.CharField(
        max_length=35,
        verbose_name='Телефон',
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to='users/avatar',
        verbose_name='Аватар',
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length = 50,
        blank=True,
        null=True,
    )
    token = models.CharField(max_length=100,
                             verbose_name='Token',
                             blank=True,
                             null=True, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []