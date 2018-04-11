"""Forms of basic app."""
from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """Used for signing up user.

    Attributes:
        email (TYPE): Email Field
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = models.User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user
        return None
