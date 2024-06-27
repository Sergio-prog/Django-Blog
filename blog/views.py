from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.models import Article


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


def get_article(request, link: str):
    article = Article.objects.get(link=link)
    print(article)
    return render(request, "blog/article.html", {"article": article})

