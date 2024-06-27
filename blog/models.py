import random

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.http import urlencode
from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class UserPermissions(models.Model):
    class Meta:
        permissions = [
            ("can_read_blogs", "Can read blogs")
        ]


class Article(models.Model):
    @staticmethod
    def _random_identifier():
        return random.randint(100000, 999999)

    @classmethod
    def generate_link(cls, title: str):
        identifier = str(cls._random_identifier())
        return urlencode(title.replace(" ", "-") + identifier)

    @classmethod
    def create(cls, title: str, body: str):
        return Article(title=title, body=body, link=cls.generate_link(title))

    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    body = models.CharField()
    created_at = models.DateTimeField("date published", auto_now=True)
    link = models.CharField(max_length=120)
