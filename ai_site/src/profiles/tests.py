from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

# Create your tests here.
from src.profiles.models import UserNet


class UserApiTestCase(APITestCase):

    def get_auth_tokens(self, username: str, password: str) -> dict:
        url = reverse('jwt-create')
        user = UserNet.objects.create_user(username=f'{username}', password=f'{password}')
        user.save()
        response = self.client.post(url, {'username': f'{username}', 'password': f'{password}'})
        return response.data

    # def test_get_unauthorized(self):
    #     url = reverse('public-user', args=[1])
    #
    #
    #     response = self.client.get(url)
    #     # print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data)

    def test_get_authorized(self):
        url = reverse('public-user', args=[1])
        print(url)
        self.get_auth_tokens(username='admin', password='admin')
        client = APIClient()
        create_token = self.get_auth_tokens(username='admin1', password='admin1').get('access')
        print(create_token)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + f'{create_token}')
        resp = self.client.get(url)
        print(resp.data, resp.status_code)
