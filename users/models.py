import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField("Номер телефона", max_length=30, unique=True, null=True, blank=True)
    photo = models.URLField("Фото пользователя", null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("phone",)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self) -> str:
        return f"Username: {self.username}"
