from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        user = self.set_base_user_data(email, password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.set_base_user_data(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def set_base_user_data(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
