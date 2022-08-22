# from django.contrib.auth import get_user_model
# from django.db import models

# User = get_user_model()


# class Tag(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     color = models.CharField(verbose_name='Цветовой HEX-код', unique=True, max_length=7)
#     slug = models.SlugField(unique=True)

#     class Meta:
#         ordering = ('id',)
#         verbose_name = 'Тег'
#         verbose_name_plural = 'Теги'

#     def __str__(self):
#         return self.name


# class Ingredient(models.Model):
#     name = models.CharField('Название ингридиента', max_length=256)
#     measurement_unit = models.CharField('Единица измерения', max_length=256)

#     class Meta:
#         verbose_name = 'Ингредиент'
#         verbose_name_plural = 'Ингредиенты'
#         ordering = ('id',)

#     def __str__(self):
#         return f'{self.name}'


# class Recipe(models.Model):
#     name = models.CharField('Название', max_length=256)
#     text = models.TextField('Описание',)
#     author = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True,
#         related_name='recipes', verbose_name='Автор',
#     )
#     image = models.ImageField('Картинка',  upload_to='recipes/')
#     ingredients = models.ManyToManyField(
#         Ingredient,
#         through='QuantityofIngredients', 
#         related_name='recipes',
#         verbose_name='Ингредиенты'
#     )
#     tags = models.ManyToManyField(
#         Tag,
#         related_name='recipes',
#         blank=True,
#         verbose_name='Теги'
#     )
#     pub_date = models.DateTimeField(
#         'Дата публикации', auto_now_add=True
#     )

#     class Meta:
#         verbose_name = 'Рецепт'
#         verbose_name_plural = 'Рецепты'
#         ordering = ['-pub_date',]

#     def __str__(self):
#         return self.name


# class QuantityofIngredients(models.Model):
#     ingredient = models.ForeignKey(
#         Ingredient, on_delete=models.CASCADE,
#         related_name='quantity_of_ingredients',
#         verbose_name='Ингредиент',
#     )
#     recipe = models.ForeignKey(
#         Recipe, on_delete=models.CASCADE,
#         related_name='quantity_of_ingredients',
#         verbose_name='рецепт',
#     )
#     amount = models.PositiveIntegerField(
#         verbose_name='количество ингредиента',
#         # validators=(MinValueValidator(
#         #     INGREDIENT_MIN_AMOUNT,
#         #     message=INGREDIENT_MIN_AMOUNT_ERROR.format(
#         #         min_value=INGREDIENT_MIN_AMOUNT
#         #     )
#         # ),)
#     )

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['recipe', 'ingredient'],
#                 name='unique_recipe_ingredient',
#             )
#         ]
#         verbose_name = 'Количество ингредиентов'
#         ordering = ['id',]

#     # def __str__(self):
#     #     return f'{self.recipe.name} - {self.ingredient.name}'

#     def __str__(self):
#         return (
#             f'{self.ingredient.name} - {self.amount}'
#             f' ({self.ingredient.measurement_unit})'
#         )


from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Tag(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name='Название тега'
    )
    color = models.CharField(
        verbose_name='Цветовой HEX-код', unique=True, max_length=7
    )
    slug = models.SlugField(
        max_length=100, unique=True, verbose_name='Уникальный слаг'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name='Название ингредиента'
    )
    measurement_unit = models.CharField(
        max_length=100, verbose_name='Единица измерения'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='recipes', verbose_name='Автор рецепта'
    )
    name = models.CharField(max_length=100, verbose_name='Название рецепта')
    image = models.ImageField(
        upload_to='recipes/', verbose_name='Картинка рецепта'
    )
    text = models.TextField(max_length=200, verbose_name='Описание рецепта')
    ingredients = models.ManyToManyField(
        Ingredient, through='IngredientQuantity', verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag, verbose_name='Теги'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления (в минутах)',
        validators=[
            MinValueValidator(
                1, message='Время приготовления должно быть больше 0!'
            )
        ]
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт'
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(1, message='Количество должно быть больше 0!')
        ]
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['ingredient', 'recipe'],
                name='unique_ingredients_in_recipe'
            )
        ]
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='favorites', verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='favorites', verbose_name='Рецепт'
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_recipe_in_favorite'
            )
        ]
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='shopping_carts', verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='shopping_carts', verbose_name='Рецепт'
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_recipe_in_shopping_cart'
            )
        ]
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзины покупок'