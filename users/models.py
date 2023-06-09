from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AccountManager(BaseUserManager):
    """Creates user or superuser for our database"""
    def create_user(self, email, fullname, password=None):
        """Create user"""
        if not email:
            raise ValueError('User must provide email!')

        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self.db)

        return user

    def create_superuser(self, email, fullname, password=None):
        """Create superuser"""
        user = self.create_user(email=email, fullname=fullname, password=password)

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """Define account information in database"""
    email = models.EmailField(max_length=60, unique=True, verbose_name='Email Address')
    fullname = models.CharField(max_length=30, unique=True)
    date_join = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.email
