from django.http import HttpResponse
from django.template import loader
import os
from lockdown.decorators import lockdown

# Create your views here.

# Add the repo you want to display
repo_list_nLatt = ["nLatt",
                    ["date_a_scientist",
                     "boulder_dash",
                     "Game_Of_Life",
                     "machine_learning_codeacademy",
                     "Game_Of_Life",
                     "machine_learning_codeacademy",
                     "Game_Of_Life",
                     "machine_learning_codeacademy",
                    ]
                  ]

variables = {
    "user": repo_list_nLatt[0],
    "repos": repo_list_nLatt[1],
    "card_width": 300,
}

@lockdown()
def main(request):
    filename = os.path.join("portfolio", "main.html")
    template = loader.get_template(filename)

    return HttpResponse(template.render(variables))
