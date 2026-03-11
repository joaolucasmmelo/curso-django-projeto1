from django.shortcuts import render
# Create your views here.


def home_view(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'João Lucas',
        'idade': 21,
        'sabor': 'energetico pae',
    })
