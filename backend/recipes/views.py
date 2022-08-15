from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Tag, Recipe
from .permissions import IsOwnerOrReadOnly
from .serializers import TagSerializer, RecipeSerializer, IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]
    serializer_class = IngredientSerializer

#    def get_queryset(self):
#        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'),)
#        return post.comments.all()

#    def perform_create(self, serializer):
#        post_id = self.kwargs.get('post_id')
#        post = get_object_or_404(Post, pk=post_id)
#        serializer.save(
#            author=self.request.user, post=post)
