from django.db import router
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, RecipeViewSet, IngredientViewSet

router = DefaultRouter()

router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'ingredients', IngredientViewSet,
                basename='ingredient')


urlpatterns = [
    # path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
