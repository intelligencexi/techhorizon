
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import Registrant
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new registrant and save it to the database
            Registrant.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                interest=form.cleaned_data['interest']
            )
            messages.success(request, "Registration successful.")
            return redirect('register')  # Redirect to clear the form or a success page
        else:
            messages.error(request, "There was an error with your registration.")
    return render(request, 'events/register.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authenticate based on email; adjust if email is username
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('home')  # Redirect to a home page
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "There was an error with your login.")
    return render(request, 'events/login.html')



def home(request):
    return render(request, 'events/home.html')
