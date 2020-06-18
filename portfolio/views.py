from django.http import HttpResponse
from django.template import loader
import os

# Create your views here.
repo_list = ["date-a-scientist", "Game_Of_Life", "machine_learning_codeacademy", "Game_Of_Life", "machine_learning_codeacademy", "Game_Of_Life", "machine_learning_codeacademy"]

variables = {
    "repos": repo_list,
    "user": "nLatt"
}

def header(request):
    filename = os.path.join("portfolio", "main.html")
    template = loader.get_template(filename)
    return HttpResponse(template.render(variables))
