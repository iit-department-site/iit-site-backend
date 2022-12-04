from rest_framework import serializers

from .models import UserNet, Technology


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
            "user_permissions",
            "first_login",
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    """ Output subscribers 
    """

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ('id', 'username', 'avatar')


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"


class TechnologyImageSerializer(serializers.ModelSerializer):
    """Output info about user
    """
    image = serializers.ImageField()

    class Meta:
        model = Technology
        fields = ('image',)
