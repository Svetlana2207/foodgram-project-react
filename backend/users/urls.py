from django.urls import include, path
from rest_framework import routers

from .views import APITokenDelete, APIToken, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
#    path('auth/token/logout/', APITokenDelete.as_view(), name='logout'),
#    path('auth/token/login/', APIToken.as_view(), name='login'),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('', include(router.urls)),
]
