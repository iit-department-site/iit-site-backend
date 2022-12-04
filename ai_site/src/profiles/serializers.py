from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Output info about user
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "first_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class UserAvatarSerializer(serializers.ModelSerializer):
    """Output info about user
    """
    avatar = serializers.ImageField()

    class Meta:
        model = UserNet
        fields = ('avatar',)


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """Output public info about user
    """

    class Meta:
        model = UserNet
        exclude = (
            "email",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    """ Output subscribers 
    """

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ('id', 'username', 'avatar')
