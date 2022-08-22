from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True, verbose_name='Почта'
    )
    username = models.CharField(
        max_length=150, unique=True, verbose_name='Имя пользователя'
    )
    first_name = models.CharField(
        max_length=150, verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150, verbose_name='Фамилия'
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=150, null=True, blank=False,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower', verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following', verbose_name='Автор подписки'
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_follow'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='prevent_self_follow'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
