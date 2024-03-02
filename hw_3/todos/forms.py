from django import forms
from django.forms import DateInput


class CreateList(forms.Form):
    Дело = forms.CharField(min_length=1, max_length=255, required=True)
    Описание = forms.CharField(min_length=0, max_length=1000, required=True)
    Дата = forms.DateField(required=True, widget=DateInput({'type': 'date'}))
    Статус = forms.BooleanField(required=False)

