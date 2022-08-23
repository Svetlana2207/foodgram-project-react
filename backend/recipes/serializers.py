# from drf_extra_fields.fields import Base64ImageField
# from .models import Tag, Recipe, Ingredient, QuantityofIngredients
# from rest_framework import serializers


# from users.serializers import CustomUserSerializer

# class IngredientSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Ingredient
#         # fields = '__all__'
#         fields = ('id', 'name', 'measurement_unit')


# class TagSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Tag
#         fields = ('id', 'name', 'slug', 'color')


# class QuantityofIngredients(serializers.ModelSerializer):
#     # name = serializers.ReadOnlyField(source='ingredient.name')
#     # measurement_unit = serializers.ReadOnlyField(
#     #     source='ingredient.measurement_unit.name'
#     # )
#     id = serializers.PrimaryKeyRelatedField
#         (queryset=Ingredient.objects.all())

#     class Meta:
#         model = QuantityofIngredients
#         fields = ('id', 'amount')


# # class RecipeSerializer(serializers.ModelSerializer):
# #     author = serializers.SlugRelatedField(slug_field='username',
# #                                           read_only=True)

# #     class Meta:
# #         model = Recipe
# #         fields = ('id', 'text', 'author', 'image', 'tag', 'pub_date')


# class RecipeIngredientReadSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField(source='ingredient.id')
#     name = serializers.ReadOnlyField(source='ingredient.name')
#     measurement_unit = serializers.ReadOnlyField(
#         source='ingredient.measurement_unit')

#     class Meta:
#         model = QuantityofIngredients
#         fields = ('id', 'name', 'measurement_unit', 'amount',)


# class RecipeReadSerializer(serializers.ModelSerializer):
#     tags = TagSerializer(many=True, read_only=True)
#     author = CustomUserSerializer(read_only=True)
#     ingredients = serializers.SerializerMethodField(read_only=True)
#     is_favorited = serializers.SerializerMethodField(read_only=True)
#     is_in_shopping_cart = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Recipe
#         fields = (
#             'id', 'name', 'tags', 'author', 'ingredients', 'is_favorited',
#             'is_in_shopping_cart', 'image', 'text', 'cooking_time',
#         )

#     def get_ingredients(self, obj):
#         queryset = QuantityofIngredients.objects.filter(recipe=obj)
#         return RecipeIngredientReadSerializer(queryset, many=True).data

#     # def get_is_in_shopping_cart(self, obj):
#     #     request = self.context.get('request')
#     #     if not request or request.user.is_anonymous:
#     #         return False
#     #     return ShoppingCart.objects.filter(
#     #         user=request.user, recipe=obj).exists()

#     # def get_is_favorited(self, obj):
#     #     request = self.context.get('request')
#     #     if not request or request.user.is_anonymous:
#     #         return False
#     #     return Favorite.objects.filter
#               (user=request.user, recipe=obj).exists()


# class RecipeIngredientWriteSerializer(serializers.ModelSerializer):
#     id = serializers.PrimaryKeyRelatedField
#      (queryset=Ingredient.objects.all())
#     amount = serializers.IntegerField()

#     class Meta:
#         model = QuantityofIngredients
#         fields = ('id', 'amount')


# class RecipeSerializer(serializers.ModelSerializer):
#     tags = serializers.PrimaryKeyRelatedField(
#         queryset=Tag.objects.all(), many=True)
#     ingredients = RecipeIngredientWriteSerializer(many=True)
#     author = QuantityofIngredients(read_only=True)
#     image = Base64ImageField()

#     class Meta:
#         model = Recipe
#         fields = ('id', 'author', 'ingredients', 'tags', 'image',
#                   'name', 'text', 'cooking_time')

#     def validate(self, data):
#         ingredients = self.initial_data.get('ingredients')
#         ingredients_list = []
#         for ingredient in ingredients:
#             ingredient_id = ingredient['id']
#             if ingredient_id in ingredients_list:
#                 raise serializers.ValidationError({
#                     'ingredient': 'Ингредиенты должны быть уникальными!'
#                 })
#             ingredients_list.append(ingredient_id)
#             amount = ingredient['amount']
#             if int(amount) <= 0:
#                 raise serializers.ValidationError({
#                     'amount': 'Количество ингредиента > нуля!'
#                 })

#         cooking_time = self.initial_data.get('cooking_time')
#         if int(cooking_time) <= 0:
#             raise serializers.ValidationError({
#                 'cooking_time': 'Время приготовления > нуля!'
#             })
#         return data

#     # @staticmethod
#     # def create_ingredients(ingredients, recipe):
#     #     for ingredient in ingredients:
#     #         CountOfIngredient.objects.create(
#     #             recipe=recipe, ingredient=ingredient['id'],
#     #             amount=ingredient['amount'])

#     # @staticmethod
#     # def create_tags(tags, recipe):
#     #     for tag in tags:
#     #         recipe.tags.add(tag)

#     # def create(self, validated_data):
#     #     author = self.context.get('request').user
#     #     tags = validated_data.pop('tags')
#     #     ingredients = validated_data.pop('ingredients')
#     #     recipe = Recipe.objects.create(author=author, **validated_data)
#     #     self.create_tags(tags, recipe)
#     #     self.create_ingredients(ingredients, recipe)
#     #     return recipe

#     # def update(self, instance, validated_data):
#     #     instance.tags.clear()
#     #     CountOfIngredient.objects.filter(recipe=instance).delete()
#     #     self.create_tags(validated_data.pop('tags'), instance)
# #     self.create_ingredients(validated_data.pop('ingredients'), instance)
#     #     return super().update(instance, validated_data)

#     # def to_representation(self, instance):
#     #     request = self.context.get('request')
#     #     context = {'request': request}
#     #     return RecipeReadSerializer(
#     #         instance, context=context).data


# # class RepresentationSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Recipe
# #         fields = ('id', 'name', 'image', 'cooking_time')


# # class ShoppingCartSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = ShoppingCart
# #         fields = ('user', 'recipe')

# #     def to_representation(self, instance):
# #         request = self.context.get('request')
# #         context = {'request': request}
# #         return RepresentationSerializer(
# #             instance.recipe, context=context).data


# # class FavoriteSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Favorite
# #         fields = ('user', 'recipe')

# #     def to_representation(self, instance):
# #         request = self.context.get('request')
# #         context = {'request': request}
# #         return RepresentationSerializer(
# #             instance.recipe, context=context).data


from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from users.serializers import CustomUserSerializer

from .models import (Favorite, Ingredient, IngredientQuantity, Recipe,
                     ShoppingCart, Tag)

TAGS_UNIQUE_ERROR = 'Теги не могут повторяться!'
TAGS_EMPTY_ERROR = 'Выберите минимум один тег!'
INGREDIENTS_UNIQUE_ERROR = 'Ингредиенты не могут повторяться!'
INGREDIENTS_EMPTY_ERROR = 'Выберите минимум 1 ингредиент!'
INGREDIENT_MIN_AMOUNT_ERROR = 'Количество ингредиента не может быть меньше 1!'
INGREDIENT_DOES_NOT_EXIST = 'Такого ингредиента не существует!'
INGREDIENT_MIN_AMOUNT = 1
COOKING_TIME_MIN_VALUE = 1
COOKING_TIME_MIN_ERROR = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class IngredientQuantitySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
    )

    class Meta:
        model = IngredientQuantity
        fields = ('id', 'name', 'measurement_unit', 'amount')


class RecipeListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = CustomUserSerializer(read_only=True)
    ingredients = serializers.SerializerMethodField(read_only=True)
    is_favorited = serializers.SerializerMethodField(read_only=True)
    is_in_shopping_cart = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients', 'is_favorited',
            'is_in_shopping_cart', 'name', 'image', 'text', 'cooking_time'
        )

    def get_ingredients(self, obj):
        ingredients = IngredientQuantity.objects.filter(recipe=obj)
        return IngredientQuantitySerializer(ingredients, many=True).data

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return Favorite.objects.filter(user=request.user, recipe=obj).exists()

    def get_is_in_shopping_cart(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return ShoppingCart.objects.filter(
            user=request.user, recipe=obj).exists()


class IngredientWriteSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all()
    )
    amount = serializers.IntegerField()

    class Meta:
        model = IngredientQuantity
        fields = ('id', 'amount')


class RecipeWriteSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    ingredients = IngredientWriteSerializer(many=True)
    author = CustomUserSerializer(read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'id', 'author', 'ingredients', 'tags', 'image',
            'name', 'text', 'cooking_time'
        )

    def validate(self, data):
        if data['cooking_time'] < COOKING_TIME_MIN_VALUE:
            raise serializers.ValidationError(COOKING_TIME_MIN_ERROR)
        if len(data['tags']) == 0:
            raise serializers.ValidationError(TAGS_EMPTY_ERROR)
        if len(data['tags']) > len(set(data['tags'])):
            raise serializers.ValidationError(TAGS_UNIQUE_ERROR)
        if len(data['ingredients']) == 0:
            raise serializers.ValidationError(INGREDIENTS_EMPTY_ERROR)
        id_ingredients = []
        for ingredient in data['ingredients']:
            if ingredient['amount'] < INGREDIENT_MIN_AMOUNT:
                raise serializers.ValidationError(
                    INGREDIENT_MIN_AMOUNT_ERROR.format(
                        min_value=INGREDIENT_MIN_AMOUNT,
                    )
                )
            id_ingredients.append(ingredient['id'])
        if len(id_ingredients) > len(set(id_ingredients)):
            raise serializers.ValidationError(INGREDIENTS_UNIQUE_ERROR)
        return data

    # def validate(self, data):
    #     ingredients = self.initial_data.get('ingredients')
    #     if not ingredients:
    #         raise serializers.ValidationError({
    #             'ingredients': 'Невозможно приготовить из воздуха!
    #             Выберите минимум 1 ингредиент!)'
    #         })
    #     ingredients_list = []
    #     for ingredient in ingredients:
    #         ingredient_id = ingredient['id']
    #         if ingredient_id in ingredients_list:
    #             raise serializers.ValidationError({
    #                 'ingredients': 'Ингредиенты должны быть уникальными!'
    #             })
    #         ingredients_list.append(ingredient_id)
    #         amount = ingredient['amount']
    #         if int(amount) <= 0:
    #             raise serializers.ValidationError({
    #                 'amount': 'Сколько вешать в граммах?
    #                 Количество ингредиента должно быть больше нуля!'
    #             })

    #     tags = self.initial_data.get('tags')
    #     if not tags:
    #         raise serializers.ValidationError({
    #             'tags': 'Нужно выбрать хотя бы один тэг!'
    #         })
    #     tags_list = []
    #     for tag in tags:
    #         if tag in tags_list:
    #             raise serializers.ValidationError({
    #                 'tags': 'Тэги должны быть уникальными!'
    #             })
    #         tags_list.append(tag)

    #     cooking_time = self.initial_data.get('cooking_time')
    #     if int(cooking_time) <= 0:
    #         raise serializers.ValidationError({
    #             'cooking_time': 'Время приготовления должно быть больше 0!'
    #         })
    #     return data

    def create_ingredients(self, ingredients, recipe):
        for ingredient in ingredients:
            ingredient_id = ingredient['id']
            amount = ingredient['amount']
            IngredientQuantity.objects.create(
                recipe=recipe, ingredient=ingredient_id, amount=amount
            )

    def create_tags(self, tags, recipe):
        for tag in tags:
            recipe.tags.add(tag)

    def create(self, validated_data):
        author = self.context.get('request').user
        tags = validated_data.pop('tags')
        ingredients = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(author=author, **validated_data)
        self.create_tags(tags, recipe)
        self.create_ingredients(ingredients, recipe)
        return recipe

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.cooking_time = validated_data.get(
            'cooking_time', instance.cooking_time
        )

        instance.tags.clear()
        tags = validated_data.get('tags')
        self.create_tags(tags, instance)

        IngredientQuantity.objects.filter(recipe=instance).all().delete()
        ingredients = validated_data.get('ingredients')
        self.create_ingredients(ingredients, instance)

        instance.save()
        return instance

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RecipeListSerializer(
            instance, context=context).data


class RecipeRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('user', 'recipe')

    def validate(self, data):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        recipe = data['recipe']
        if Favorite.objects.filter(user=request.user, recipe=recipe).exists():
            raise serializers.ValidationError({
                'status': 'Рецепт уже есть в избранном!'
            })
        return data

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RecipeRepresentationSerializer(
            instance.recipe, context=context).data


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('user', 'recipe')

    def validate(self, data):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        recipe = data['recipe']
        if ShoppingCart.objects.filter(
            user=request.user, recipe=recipe
        ).exists():
            raise serializers.ValidationError({
                'status': 'Рецепт уже есть в списке покупок!'
            })
        return data

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RecipeRepresentationSerializer(
            instance.recipe, context=context).data
