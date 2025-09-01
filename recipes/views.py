from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'recipes/home.html', context={
        "nome": "Anderson"
    })

def contato(request):
    return HttpResponse("CONTATO")


def sobre(request):
    return HttpResponse("SOBRE")