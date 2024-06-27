from django.contrib import admin
from django.contrib.auth.models import User

from blog.models import BlogUser, Article

# Register your models here.
admin.site.register(BlogUser)
admin.site.register(Article)
