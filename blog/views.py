from django.http import HttpResponse
from . import models
from django.template import loader, Context
import datetime


def blog(request):
    posts = models.Post.objects.all()
    template = loader.get_template('blog/blog.html')
    context = {"posts": posts}
    return HttpResponse(template.render(context))

def news(request):
    posts = models.Post.objects.all().filter(date_published=datetime.date.today())
    t = loader.get_template('blog/news.html')
    context = {"posts": posts}
    return HttpResponse(t.render(context))