from django import forms
from . models import ProfileModel

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=[
            'url_code',
            'author',
            'icon',
            'introduce',
        ]