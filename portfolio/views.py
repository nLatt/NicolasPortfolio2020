from django.http import HttpResponse
from django.template import loader
import os

# Create your views here.

# Add the repo you want to display
repo_list_nLatt = ["nLatt", ["date-a-scientist", "GameOfLife", "machine_learning_codeacademy", "pokemon_eda", "nLatt/boulder_dash", "nLatt/Catch_Ball"]]

variables = {
    "user": repo_list_nLatt[0],
    "repos": repo_list_nLatt[1],
}

def header(request):
    filename = os.path.join("portfolio", "main.html")
    template = loader.get_template(filename)

    return HttpResponse(template.render(variables))
