from django.urls import path
from .views import search_person

urlpatterns = [
    path('', search_person, name='search_person'),
]
