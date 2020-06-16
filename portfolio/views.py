from django.http import HttpResponse
from django.template import Context, loader
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'relative/path/to/file/you/want')

# Create your views here.

def header(request):
    filename = os.path.join(dirname, 'templates\\portfolio\\hello_world.html')
    template = loader.get_template(filename)
    return HttpResponse(template.render())
