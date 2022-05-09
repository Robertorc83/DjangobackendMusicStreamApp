from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    Name = models.CharField(max_length=None)
    lastName = models.CharField(max_length=None)
    genre = models.CharField(max_length=None)
    age = models.IntegerField(default=0)
    Favorite_Genre = models.CharField(max_length=None)
    Favorite_Genre2 = models.CharField(max_length=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    is_admin = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)
    
    
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin