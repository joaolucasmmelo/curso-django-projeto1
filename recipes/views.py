from django.shortcuts import render
# Create your views here.


def home_view(request):
    return render(request, 'recipes/home.html', context={
        'name': 'joao',
        'idade': 21,
        'sabor': 'energetico pae',
    })
