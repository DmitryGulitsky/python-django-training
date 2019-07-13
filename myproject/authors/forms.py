from django import forms

from .models import AuthorsModel

class AuthorForm(forms.ModelForm):

    class Meta:
        model = AuthorsModel
        fields = ('first_name', 'last_name', 'email')
