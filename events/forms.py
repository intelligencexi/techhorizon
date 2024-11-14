from django import forms

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
