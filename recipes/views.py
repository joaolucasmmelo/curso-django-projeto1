from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request):
    return render(request, 'recipes/home.html', context={
        'name': 'joao',
        'idade': 21,
        'sabor': 'energetico pae',
    })
    # Return HTTP Response


def sobre_view(request):
    return HttpResponse('Sobre Page')
    # Return HTTP Response


def contato_view(request):
    return HttpResponse('Contato Page')
    # Return HTTP Response
