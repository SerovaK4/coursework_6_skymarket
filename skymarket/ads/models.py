import datetime
from django.utils import timezone
from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название товара", default="Не указано")
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="Цена товара", default=0)
    description = models.CharField(max_length=200, verbose_name="Описание товара", **NULLABLE)
    image = models.ImageField(upload_to="media/", verbose_name="Фото товара", **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}: {self.description}'

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comment(models.Model):
    text = models.TextField(max_length=400, default=None)
    created_at = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.author}: {self.text}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
