from django import forms
from django.db.models import CASCADE
from django.forms import DateInput

from . import models
from .models import Todo


class CreateList(forms.Form):
    Дело = forms.CharField(min_length=1, max_length=255, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите дело'}))
    Описание = forms.CharField(min_length=0, max_length=1000, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите описание'}))
    Дата = forms.DateField(required=True, widget=forms.DateInput({'type': 'date'}))
    Статус = forms.BooleanField(required=False)


class CreateCategory(forms.Form):
    Название = forms.CharField(min_length=1, max_length=255, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название категории'}))
    Описание = forms.CharField(min_length=0, max_length=1000, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите описание'}))
