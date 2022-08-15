from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    CHOICE_ROLE = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=254,
        unique=True,
    )
    username = models.SlugField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )
    role = models.TextField(
        'Пользовательская роль',
        max_length=40,
        choices=CHOICE_ROLE,
        default='user',
        blank=True,
    )
    password = models.CharField(
        'Пароль',
        max_length=150,
        null=True,
        blank=False,
    )

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_user(self):
        return self.role == 'user'

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.username
