from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from blog.models import Article, BlogUser


# Create your views here.
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "articles"

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.all()


# @permission_required("can_read_blogs")
def index(request):
    return render(request, "blog/index.html", {"articles": Article.objects.all()})


# Not implemented yet
def profile(request, id):
    return render(request, "blog/index.html", {"articles": Article.objects.all()})


def get_article(request, link: str):  # TODO: Добавить проверку на method ендпоинта
    article = Article.objects.get(link=link)
    print(article)
    return render(request, "blog/article.html", {"article": article})


def get_articles_by_user(request, id: str):
    ...


def create_article(request):
    if request.method == "GET":
        return render(request, "blog/write_article.html")
    elif request.method == "POST":
        body = request.body
        required_fields = ("title", "body")

        not_provided_fields = []
        for field in required_fields:
            if not body.get(field):
                not_provided_fields.append(field)

        if not_provided_fields:
            not_provided_fields = ', '.join(not_provided_fields)
            messages.error(request, f"These fields are not provided (or empty): {not_provided_fields}")

        Article.create(body.title, body.body)
        messages.success(request, "Successfully created new article")
        return render(request, "blog/write_article.html")


def edit_profile(request):
    ...


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BlogUser
        fields = UserCreationForm.Meta.fields


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
