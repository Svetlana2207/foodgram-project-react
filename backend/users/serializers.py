from django.contrib.auth import get_user_model
from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

from .models import UserSubscription
# from .models import User
User = get_user_model()


class UserSerializer(UserCreateSerializer):
    is_subscribed = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'password', 'is_subscribed')

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return UserSubscription.objects.filter(
            subscriber=user, subscription=obj
        ).exists()

