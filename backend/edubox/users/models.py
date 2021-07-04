from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class User (AbstractUser):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #permission_classes = (IsAuthenticated,)
    objects = CustomUserManager()

    name = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to = 'profileImgs/', blank=True, null=True)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.email