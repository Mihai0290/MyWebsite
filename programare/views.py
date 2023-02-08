from django.http import HttpResponse
from django.template import loader

def programare(request):
    template = loader.get_template("programare/programare.html")
    return HttpResponse(template.render())

def lectii(request):
    template = loader.get_template("programare/lectii.html")
    return HttpResponse(template.render())

def lectie(request, lesson):
    template = loader.get_template("programare/lectie" + str(lesson) +".html")
    return HttpResponse(template.render())
