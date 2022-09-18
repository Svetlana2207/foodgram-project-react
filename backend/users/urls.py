from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import FollowApiView, FollowListAPIView

router = DefaultRouter()

urlpatterns = [
    path('users/<int:id>/subscribe/', FollowApiView.as_view(),
         name='subscribe'),
    path('users/subscriptions/', FollowListAPIView.as_view(),
         name='subscription'),
    # path('docs/',
    #     TemplateView.as_view(template_name='docs/redoc.html'),
    #     name='redoc'
    #     ),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
