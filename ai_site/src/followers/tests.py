from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.
from src.followers.models import Follower
from src.followers.serializers import ListFollowerSerializer
from src.profiles.models import UserNet


class UserApiTestCase(APITestCase):

    def setUp(self):
        user1 = UserNet.objects.create_user(username="Mark", password='admin')
        user2 = UserNet.objects.create_user(username="Mark2", password='admin2')
        follow1 = Follower.objects.create(user=user1, subscriber=user2)

    def test_unautorizer_status_code(self):
        url = reverse('follower', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data)
