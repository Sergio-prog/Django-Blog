from django.test import TestCase
from django.urls import reverse

from blog.models import Article


# Create your tests here.
class ArticleTests(TestCase):
    def test_create_article(self):  # TODO
        title = "Test case (Django, Unittest) 123456789"
        body = "Hey, testing!"
        new_article = Article.create(user=self, title=title, body=body)
