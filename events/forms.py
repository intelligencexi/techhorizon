from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    interest = forms.ChoiceField(choices=[
        ('software-development', 'Software Development'),
        ('cybersecurity', 'Cybersecurity'),
        ('data-science', 'Data Science'),
        ('ai', 'Artificial Intelligence'),
    ], required=True)

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_superuser = True  # Mark as superuser
        user.is_staff = True      # Mark as staff
        if commit:
            user.save()
        return user