# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated, AllowAny

# from .models import Ingredient, Tag, Recipe
# from .permissions import IsOwnerOrReadOnly
# from .serializers import (RecipeReadSerializer, TagSerializer,
#                          RecipeSerializer, IngredientSerializer,
#                          RecipeReadSerializer)

# class RecipeViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]
#     queryset = Recipe.objects.all()
#     def get_serializer_class(self):
#         if self.action in ('list', 'retrieve'):
#             return RecipeReadSerializer
#         return RecipeSerializer

#     @staticmethod
#     def post_method_for_action(request, pk, serializers):
#         data = {'user': request.user.id, 'recipe': pk}
#         serializer = serializers(data=data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class TagViewSet(viewsets.ReadOnlyModelViewSet):
#     pagination_class = None
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# class IngredientViewSet(viewsets.ModelViewSet):
#     pagination_class = None
#     queryset = Ingredient.objects.all()
#     #permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]
#     serializer_class = IngredientSerializer


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .filters import IngredientSearchFilter, RecipeFilter
from .models import (Favorite, Ingredient, IngredientQuantity, Recipe,
                     ShoppingCart, Tag)
from .permissions import IsAuthorOrReadOnly
from .serializers import (FavoriteSerializer, IngredientSerializer,
                          RecipeListSerializer, RecipeWriteSerializer,
                          ShoppingCartSerializer, TagSerializer)


class TagsViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer
    pagination_class = None


class IngredientsViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = IngredientSerializer
    filter_backends = [IngredientSearchFilter]
    search_fields = ('^name',)
    pagination_class = None


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeListSerializer
        return RecipeWriteSerializer

    @action(detail=True, permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        data = {'user': request.user.id, 'recipe': pk}
        serializer = FavoriteSerializer(
            data=data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @favorite.mapping.delete
    def delete_favorite(self, request, pk):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        favorite = get_object_or_404(
            Favorite, user=user, recipe=recipe
        )
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk):
        data = {'user': request.user.id, 'recipe': pk}
        serializer = ShoppingCartSerializer(
            data=data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @shopping_cart.mapping.delete
    def delete_shopping_cart(self, request, pk):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        shopping_cart = get_object_or_404(
            ShoppingCart, user=user, recipe=recipe
        )
        shopping_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        ingredients = IngredientQuantity.objects.filter(
            recipe__shopping_carts__user=request.user).values(
            'ingredient__name', 'ingredient__measurement_unit', 'amount'
        )
        shopping_cart = '\n'.join([
            f'{ingredient["ingredient__name"]} - {ingredient["amount"]} '
            f'{ingredient["ingredient__measurement_unit"]}'
            for ingredient in ingredients
        ])
        filename = 'shopping_cart.txt'
        response = HttpResponse(shopping_cart, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
