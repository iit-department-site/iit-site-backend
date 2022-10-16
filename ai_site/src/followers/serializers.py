from rest_framework import serializers
from .models import Follower
from src.profiles.serializers import UserByFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):
    subscribers = UserByFollowerSerializer(many=False, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscribers',)


class AddFollowerSerializer(serializers.Serializer):
    """ add to followers"""

    pass
