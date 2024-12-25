from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    def test_create_user_email_successful(self):
        email = 'memariyan74@gmail.com'
        password = 'mohammad@123'
        user = (get_user_model().objects.create_user(
            email=email, password=password))
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        email = 'memariyan74@Gmail.com'
        user = (get_user_model().objects.create_user(
            email=email, password='mohammad@123'))
        self.assertEqual(user.email, 'memariyan74@gmail.com')

    def test_create_user_without_email_failed(self):
        with ((self.assertRaises(ValueError))):
            get_user_model().objects.create_user(
                email=None, password='mohammad@123')

    def test_create_super_user_successful(self):
        email = 'memariyan74@gmail.com'
        user = (get_user_model().objects.create_superuser(
            email=email, password='mohammad@123'))
        self.assertEqual(user.email, 'memariyan74@gmail.com')

    def test_create_recipe_successful(self):
        user = get_user_model().objects.create_user(
            email='memariyan74@gmail.com',
            password='pass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='sample recipe name',
            time_minutes=5,
            price=Decimal("5.50"),
            description='sample recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)
