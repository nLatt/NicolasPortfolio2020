from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def header(request):
    #template = loader.get_template("portfolio/hello_world.html")
    return HttpResponse("hello world!")#template.render())
