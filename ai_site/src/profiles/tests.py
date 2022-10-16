from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from src.profiles.models import UserNet
from src.profiles.serializers import GetUserNetPublicSerializer, GetUserNetSerializer, UserByFollowerSerializer


class UserByFollowerSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = UserNet.objects.create_user(username="Mark", password='admin')
        user2 = UserNet.objects.create_user(username="Mark2", password='admin2')
        data = UserByFollowerSerializer([user1, user2], many=True).data
        expected_data = [
            {
                'id': user1.id,
                'username': user1.username,
            },
            {
                'id': user2.id,
                'username': user2.username,
            }
        ]
        serialized_data = [
            {
                'id': data[0].get('id'),
                'username': data[0].get('username')
            },
            {
                'id': data[1].get('id'),
                'username': data[1].get('username')
            }
        ]
        self.assertEqual(expected_data, serialized_data)


class UserNetPrivateSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = UserNet.objects.create_user(username="Mark", password='admin', email="admin1@gmail.com")
        user2 = UserNet.objects.create_user(username="Mark2", password='admin2', email="admin2@gmail.com")
        data = GetUserNetSerializer([user1, user2], many=True).data
        expected_data = [
            {
                'id': user1.id,
                'username': user1.username,
                'email': user1.email,
            },
            {
                'id': user2.id,
                'username': user2.username,
                'email': user2.email,
            }
        ]
        serialized_data = [
            {
                'id': data[0].get('id'),
                'username': data[0].get('username'),
                'email': data[0].get('email'),
            },
            {
                'id': data[1].get('id'),
                'username': data[1].get('username'),
                'email': data[1].get('email'),
            }
        ]
        self.assertEqual(expected_data, serialized_data)


class UserNetSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = UserNet.objects.create_user(username="Mark", password='admin')
        user2 = UserNet.objects.create_user(username="Mark2", password='admin2')
        data = GetUserNetPublicSerializer([user1, user2], many=True).data
        expected_data = [
            {
                'id': user1.id,
                'username': user1.username,
            },
            {
                'id': user2.id,
                'username': user2.username,
            }
        ]
        serialized_data = [
            {
                'id': data[0].get('id'),
                'username': data[0].get('username')
            },
            {
                'id': data[1].get('id'),
                'username': data[1].get('username')
            }
        ]
        self.assertEqual(expected_data, serialized_data)


class UserApiTestCase(APITestCase):

    def setUp(self):
        self.username = "admin1"
        self.password = "admin1"
        UserNet.objects.create_user(username=f'{self.username}', password=f'{self.password}')

    def get_auth_tokens(self) -> dict:
        url = reverse('jwt-create')
        response = self.client.post(url, {'username': f'{self.username}', 'password': f'{self.password}'})
        return response.data

    def test_public_status_code(self):
        url = reverse('public-user', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)

    def test_get_authorized(self):
        url = reverse('public-user', args=[1])
        create_token = self.get_auth_tokens().get('access')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + f'{create_token}')
        resp = self.client.get(url)

    def test_private_status_code(self):
        url = reverse('private-user', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data)

    def test_private_ok_status_code(self):
        url = reverse('private-user', args=[1])
        create_token = self.get_auth_tokens().get('access')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + f'{create_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)

    def test_private_data(self):
        url = reverse('private-user', args=[1])
        create_token = self.get_auth_tokens().get('access')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + f'{create_token}')
        response = self.client.get(url)
        self.assertEqual(response.data.get('id'), 1)
        self.assertEqual(response.data.get('username'), 'admin1')
        self.assertEqual(response.data.get('gender'), 'MALE')
        self.assertEqual(response.data.get('bio'), None)
