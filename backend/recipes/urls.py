from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TagsViewSet, RecipeViewSet, IngredientsViewSet

router = DefaultRouter()

router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'tags', TagsViewSet, basename='tags')
router.register(r'ingredients', IngredientsViewSet,
                basename='ingredient')


urlpatterns = [
    path('', include(router.urls)),
]
