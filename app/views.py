from django.shortcuts import render
from .models import Person
from .forms import SearchForm

def search_person(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            results = Person.objects.filter(name__icontains=name, age=age)
    else:
        form = SearchForm()
        results = None
    return render(request, 'search.html', {'form': form, 'results': results})
