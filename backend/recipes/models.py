from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(max_length=200)
    color = models.CharField(
        verbose_name='Цветовой HEX-код', unique=True, max_length=7
    )
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-id',]
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField('Название ингридиента', max_length=256)
    measurement_unit = models.CharField(
        'Единица измерения', max_length=256)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('title',)

    def __str__(self):
        return f'{self.title}'


class QuantityofIngredients(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE,
        related_name='count_in_recipes',
        verbose_name='Ингредиент',
    )
    amount = models.PositiveIntegerField(
        'Количество',
        # validators=(MinValueValidator(
        #     INGREDIENT_MIN_AMOUNT,
        #     message=INGREDIENT_MIN_AMOUNT_ERROR.format(
        #         min_value=INGREDIENT_MIN_AMOUNT
        #     )
        # ),)
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        constraints = (models.UniqueConstraint(
                fields=('ingredient', 'amount',),
                name='unique_ingredient_amount',
            ),
        )

    def __str__(self):
        return (
            f'{self.ingredient.title} - {self.amount}'
            f' ({self.ingredient.measurement_unit})'
        )   

class Recipe(models.Model):
    name = models.CharField('Название', max_length=256)
    text = models.TextField('Описание',)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name='recipes', verbose_name='Автор',
    )
    image = models.ImageField('Картинка')
    ingredients = models.ManyToManyField(
        'QuantityofIngredients', 
        related_name='recipes',
        verbose_name='Ингридиенты'
    )
    tag = models.ManyToManyField(
        Tag, related_name='recipes', blank=True
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date',]

    def __str__(self):
        return self.text
