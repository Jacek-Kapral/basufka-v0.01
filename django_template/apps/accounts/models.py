from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model for projects generated from this template.
    """

    def __str__(self):
        return self.username
