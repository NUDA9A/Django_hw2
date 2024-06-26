from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name="аватар", **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="страна", **NULLABLE)
    verification_code = models.CharField(max_length=6, verbose_name="Ключ верификации", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
