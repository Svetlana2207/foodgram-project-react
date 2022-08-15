from django.urls import include, path
from rest_framework import routers
from djoser.views import TokenDestroyView, TokenCreateView

# from .views import UserViewSet

router = routers.DefaultRouter()
#router.register('users', UserViewSet)

urlpatterns = [
    path('', include('djoser.urls')),
    # path('auth/token/logout/', TokenDestroyView.as_view(), name='logout'),
    # path('auth/token/login/', TokenCreateView.as_view(), name='login'),
    path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
