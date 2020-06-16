from django.http import HttpResponse
from django.template import Context, loader
import os

dirname = os.path.dirname(__file__)

# Create your views here.

def header(request):
    filename = os.path.join("portfolio", "hello_world.html")
    template = loader.get_template(filename)
    return HttpResponse(template.render())
