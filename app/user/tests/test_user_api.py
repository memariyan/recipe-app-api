from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL=reverse("user:create")
GET_TOKEN_URL=reverse("user:token")

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_with_short_password_error(self):
        payload = {
            'email': 'memariyan@gmail.com',
            'password': '123',
            'name': 'Test User',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        is_user_exist = get_user_model().objects.filter(email=payload['email']).exists()
        self.assertFalse(is_user_exist)

    def test_user_with_email_exist_error(self):
        payload = {
            'email': 'memariyan@gmail.com',
            'password': 'testpass123',
            'name': 'Test User',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_user_successfully(self):
        payload = {
            'email': 'memariyan@gmail.com',
            'password': 'testpass123',
            'name': 'Test User',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_create_token_for_user_successful(self):
        user_details = {
            'email': 'memariyan@gmail.com',
            'password': 'mohammad123',
            'name': 'Test User',
        }
        create_user(**user_details)
        payload = {
            'email': user_details['email'],
            'password': user_details['password'],
        }
        res = self.client.post(GET_TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_for_user_with_bad_password_error(self):
        user_details = {
            'email': 'memariyan@gmail.com',
            'password': 'goodpas',
            'name': 'Test User',
        }
        create_user(**user_details)
        payload = {
            'email': user_details['email'],
            'password': 'badpass',
        }
        res = self.client.post(GET_TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)