from django import forms
from django.db.models import CASCADE
from django.forms import DateInput

from . import models
from .models import Todo


class CreateList(forms.Form):
    Todo = forms.CharField(min_length=1, max_length=255, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите дело'}))
    Description = forms.CharField(min_length=0, max_length=1000, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите описание'}))
    Date = forms.DateField(required=True, widget=forms.DateInput({'class': 'form-control', 'type': 'date'}))
    Status = forms.BooleanField(required=False)
