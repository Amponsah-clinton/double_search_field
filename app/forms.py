from django.forms import ModelForm
from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    age = forms.IntegerField(required=False)
