# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from django.db import models


# class User(AbstractUser):

#     CHOICE_ROLE = (
#         ('user', 'user'),
#         ('moderator', 'moderator'),
#         ('admin', 'admin'),
#     )
#     email = models.EmailField(
#         verbose_name='Адрес электронной почты',
#         max_length=254,
#         unique=True,
#     )
#     username = models.SlugField(
#         verbose_name='Имя пользователя',
#         max_length=150,
#         unique=True,
#     )
#     first_name = models.CharField(
#         'Имя',
#         max_length=150,
#         blank=True,
#     )
#     last_name = models.CharField(
#         'Фамилия',
#         max_length=150,
#         blank=True
#     )
#     role = models.TextField(
#         'Пользовательская роль',
#         max_length=40,
#         choices=CHOICE_ROLE,
#         default='user',
#         blank=True,
#     )
#     password = models.CharField(
#         'Пароль',
#         max_length=150,
#         null=True,
#         blank=False,
#     )

#     @property
#     def is_admin(self):
#         return self.role == 'admin'

#     @property
#     def is_moderator(self):
#         return self.role == 'moderator'

#     @property
#     def is_user(self):
#         return self.role == 'user'

#     class Meta:
#         ordering = ['-id']

#     def __str__(self):
#         return self.username


# class UserSubscription(models.Model):
#     subscriber = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         related_name='subscriptions',
#         on_delete=models.CASCADE
#     )
#     subscription = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         related_name='subscribers',
#         on_delete=models.CASCADE
#     )
#     subscribed_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name='subscription date'
#     )

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['subscriber', 'subscription'],
#                 name='unique_subscription',
#             )
#         ]
#         verbose_name = 'Subscription'
#         verbose_name_plural = 'Subscriptions'
#         ordering = ['-subscribed_at', 'id']

#     def __str__(self):
#         return f'{self.subscriber} - {self.subscription}'


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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

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
