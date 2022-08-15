from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
    basename='Reviews'
)
router.register(
    (
        r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments'
    ), CommentViewSet, basename='Comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
