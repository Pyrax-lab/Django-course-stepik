from django import forms 
from .models import Coment

class EmailForm(forms.Form):
    name    = forms.CharField(max_length = 255)
    email   = forms.EmailField()
    to      = forms.EmailField()
    comment = forms.CharField(widget = forms.Textarea)


class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = [ "email", "body"]

class SearchForm(forms.Form):
    search = forms.CharField()