from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Represents the users of the application."""
