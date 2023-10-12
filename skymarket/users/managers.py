from django.contrib.auth.models import (
    BaseUserManager
)

from django.db import models


class UserRole(models.TextChoices):
    USER = "user", "User"
    ADMIN = "admin", "Administrator"


# TODO здесь должен быть менеджер для модели Юзера.
# TODO Поищите эту информацию в рекомендациях к проекту
class UserManager(BaseUserManager):
    """
    Функция для создания пользователя
    """

    def create_user(self, email, first_name, last_name, phone, password=None):
        if email is None:
            raise ValueError("The email field is required!")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role="user"
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """
        Функция для создания суперпользователя
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
        )
        user.role=UserRole.ADMIN
        user.save(using=self._db)
        return user
