# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import send_mail
# from django.shortcuts import get_object_or_404
# from rest_framework import status, viewsets
# from rest_framework.decorators import action
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken

# from .models import User
# from .permissions import IsAdmin
# from .serializers import (UserSerializer)


from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from api.pagination import CustomPageNumberPagination
from users.models import Follow, User
from users.serializers import FollowListSerializer, FollowSerializer


class FollowApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        data = {'user': request.user.id, 'following': id}
        serializer = FollowSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        user = request.user
        following = get_object_or_404(User, id=id)
        follow = get_object_or_404(
            Follow, user=user, following=following
        )
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowListAPIView(ListAPIView):
    # pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        queryset = User.objects.filter(following__user=user)
        page = self.paginate_queryset(queryset)
        serializer = FollowListSerializer(
            page, many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)
