from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<str:link>/", views.get_article, name="get_article")
]
