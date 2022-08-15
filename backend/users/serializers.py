from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'password')


class TokenSerializer(serializers.ModelSerializer):
    email = serializers.SlugField()
    password = serializers.SlugField()

    class Meta:
        model = User
        fields = ('email', 'password')


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')

    def validate(self, value):
        if value['username'] == 'me':
            raise serializers.ValidationError(
                'Имя пользователя не может быть "me"!'
            )
        return value


class NoStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'role')
        read_only_fields = ('role',)
