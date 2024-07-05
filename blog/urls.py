from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    path("articles/create/", views.create_article, name="write_article"),
    path("articles/<str:link>/", views.get_article, name="get_article"),
    path("profiles/<str:id>/", views.profile, name="profile"),
]
