from django import forms
from emenu_app.models import Menu, Danie


class ErrorForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=False)