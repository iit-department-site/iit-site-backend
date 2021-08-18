from django.core.management.base import BaseCommand
from profiles.models import UserNet
from followers.models import Follower
from wall.models import Post


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        pass