from .models import Tag, Recipe, Ingredient
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ('post',)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'title', 'slug', 'color')


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'text', 'author', 'image', 'tag', 'pub_date')
