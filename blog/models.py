import math
import random

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.http import urlencode
from django.contrib.auth.models import AbstractUser

DEFAULT_PROFILE_IMAGE = "https://cdn-icons-png.flaticon.com/512/847/847969.png"


class BlogUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    profile_image = models.URLField(default=DEFAULT_PROFILE_IMAGE)


class UserPermissions(models.Model):
    class Meta:
        permissions = [
            ("can_read_blogs", "Can read blogs")
        ]


class Article(models.Model):
    @staticmethod
    def _random_identifier():
        return random.randint(100000, 999999)

    @staticmethod
    def estimate_time(body: str):
        return math.ceil(len(body.split(" ")) / 200)

    @classmethod
    def generate_link(cls, title: str):
        identifier = str(cls._random_identifier())
        return urlencode(title.replace(" ", "-") + identifier)

    @classmethod
    def create(cls, title: str, body: str, image_url: str = None):
        return Article(title=title, body=body, image_url=image_url, link=cls.generate_link(title), time_to_read=cls.estimate_time(body))

    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField("date published", auto_now=True)
    image_url = models.CharField(null=True, blank=True, default=None)
    link = models.CharField(max_length=120)
    time_to_read = models.PositiveIntegerField()
