from django.core.management.base import BaseCommand
from profiles.models import UserNet
from followers.models import Follower
from wall.models import Post


class Command(BaseCommand):
    """ для запуска теста нужно в консоль  прописать python manage.py addfake"""
    def handle(self, *args, **kwargs):
        #self.create_user()
        self.create_follower()
        self.create_post()
        self.stdout.write("Successful")
    
    def create_user(self):
        for i in range(10):
            user = UserNet.objects.create(
                username=f"test {i+22}",
                email=f'test{i}@gmail.com',
                is_active = True,
                middle_name =f"test {i}",
                phone=f'123456g78910{i}',
                gender = 1
            )
            
            user.set_password('test')
            user.save()
            
    
    
    def create_follower(self):
        user_list = UserNet.objects.order_by()[3:]
        for user in user_list:
            Follower.objects.create(user=user , subscriber_id = 1)
            
    def create_post(self):
        user_list = UserNet.objects.all()
        for user in user_list:
            Post.objects.create(text="Text post po po", user =user)
            
            