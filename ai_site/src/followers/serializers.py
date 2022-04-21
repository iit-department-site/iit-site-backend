from rest_framework import serializers
from .models import Follower
from src.profiles.serializers import UserByFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber',)


class AddFollowerSerializer(serializers.Serializer):
    """ add to followers"""

    pass
