from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

"""
    https://docs.djangoproject.com/en/3.1/topics/auth/customizing/
    Кастомная аутентификация была реализована исходя из докоментации и в соответсвии с ТЗ
"""

class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        """
            Общий метод создает и сохраняет пользователя с заданным адресом электронной почты, паролем.
        """
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
            Вызываемый метод при создании обычного пользователя, который вызывет метод _create_user.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
            Вызываемый метод при создании суперпользователя, который вызывет метод _create_user.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя, установливаем поле email для аутентификации и делаем его уникальными
    """
    username = None
    email = models.EmailField(_('email address'), blank=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
