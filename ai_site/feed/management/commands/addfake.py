from django.core.management.base import BaseCommand
from profiles.models import UserNet
from followers.models import Follower
from wall.models import Post


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        pass
    
    def create_user(self):
        for i in range(10):
            user = UserNet.objects.create(
                username=f"test {i}",
                email=f'test{i}@gmail.com',
                is_active = True,
                middle_name =f"test{i}",
                phone=f'12345678910{i}',
                gender = 1
            )
            
            user.set_password('test')
            user.save()