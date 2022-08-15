from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Recipe(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    ingredients = models.ManyToManyField(
        Tag, 
        related_name='тег',
        verbose_name='теги'
    )
    tag = models.ForeignKey(
        Tag, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        return self.text


class Ingredient(models.Model):
    title = models.CharField('Название ингридиента', max_length=256)
    measurement_unit = models.CharField(
        'Единица измерения', max_length=256)
