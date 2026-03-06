from django.urls import path

# HTTP REQUEST
from recipes.views import home_view, sobre_view, contato_view

urlpatterns = [
    path('', home_view),
    path('sobre/', sobre_view),
    path('contato/', contato_view),
]
