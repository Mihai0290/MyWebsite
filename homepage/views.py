from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template("home_page.html")
    return HttpResponse(template.render())

