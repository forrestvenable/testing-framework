from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label='Element name:', max_length=100)