from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    phone_number = models.CharField(_('Phone number of a user'),max_length=14, null=True)
