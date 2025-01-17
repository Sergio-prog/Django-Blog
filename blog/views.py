from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
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
    profile = get_object_or_404(BlogUser, id=id)
    return render(request, "blog/profile.html", {"profile": profile})


def get_article(request, link: str):  # TODO: Добавить проверку на method ендпоинта
    article = Article.objects.get(link=link)
    return render(request, "blog/article.html", {"article": article})


def get_articles_by_user(request, id: str): ...


@login_required(login_url="/accounts/login/")
def create_article(request):
    if request.method == "GET":
        return render(request, "blog/write_article.html")

    elif request.method == "POST":
        body = request.POST
        required_fields = ("title", "body")

        not_provided_fields = []
        for field in required_fields:
            if not body.get(field):
                not_provided_fields.append(field)

        if not_provided_fields:
            not_provided_fields = ", ".join(not_provided_fields)
            messages.error(request, f"These fields are not provided (or empty): {not_provided_fields}")
        else:
            Article.create(request.user, body.get("title"), body.get("body"), body.get("image"))
            messages.success(request, "Successfully created new article")

        return render(request, "blog/write_article.html")


def edit_profile(request): ...


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BlogUser
        fields = UserCreationForm.Meta.fields


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
