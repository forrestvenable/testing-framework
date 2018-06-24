from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label='Element name:', max_length=100)
    description = forms.CharField(label='Element description:', max_length=100)
    selector = forms.CharField(label='Element selector:', max_length=100)
