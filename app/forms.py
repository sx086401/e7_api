from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=20, min_length=1, required=True)
    password = forms.CharField(min_length=4, required=True)
    is_active = forms.BooleanField(required=False)
