from django import forms
from emenu_app.models import Error


class ErrorForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.EmailField(required=False)

    class Meta:
        model = Error