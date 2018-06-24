from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label='Page name:', max_length=100)
    url = forms.CharField(label='Page url:', max_length=100)