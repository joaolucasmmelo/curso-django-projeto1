from django.urls import path

# HTTP REQUEST
from recipes.views import home_view

urlpatterns = [
    path('', home_view),
]
