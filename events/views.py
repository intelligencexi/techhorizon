from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, AdminRegistrationForm
from .models import Registrant
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
import logging
logger = logging.getLogger('events')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Check if email already exists
            if Registrant.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered. Please use a different email.")
            else:
                # Save the data to the Registrant model
                Registrant.objects.create(
                    name=form.cleaned_data['name'],
                    email=email,
                    interest=form.cleaned_data['interest']
                )
                messages.success(request, "You have successfully registered for this event.")
                return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    
    # Render the form with existing errors if any
    form = RegistrationForm()
    return render(request, 'events/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Save the data to the Registrant model
#             Registrant.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 interest=form.cleaned_data['interest']
#             )
#             messages.success(request, "Registration successful.")
#             return redirect('login')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     return render(request, 'events/register.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('home')  # Redirect to a home or dashboard page
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Please correct the errors below.")
    return render(request, 'events/login.html')

def print(request):
    pass

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('landing')


def landing(request):
    return render(request, 'events/landing.html')


@login_required
def home(request):
    return render(request, 'events/home.html')

def admin_check(user):
    return user.is_superuser

@user_passes_test(admin_check)
def dashboard(request):
    registrants = Registrant.objects.all()
    return render(request, 'events/dashboard.html', {'registrants': registrants})

# def dashboard(request):
#     if not request.user.is_authenticated or not request.user.is_superuser:
#         return redirect('admin-login')
#     return render(request, 'events/dashboard.html')



def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the newly registered admin
            logger.info("New admin registered: Username: %s, Email: %s", user.username, user.email)
            messages.success(request, "Admin registered successfully!")
            return redirect('admin-login')  # Redirect to dashboard
        else:
            logger.error("Admin registration failed. Errors: %s", form.errors.as_json())
            messages.error(request, "Registration failed. Please fix the errors below.")
    else:
        form = AdminRegistrationForm()

    return render(request, 'events/adminregister.html', {'form': form})

def admin_login(request):
     if request.method == 'POST':
         form = LoginForm(request.POST)
         if form.is_valid():
             email = form.cleaned_data['email']
             password = form.cleaned_data['password']
             user = User.objects.filter(email=email).first()
             if user and user.check_password(password):
                 login(request, user)
                 messages.success(request, "Login successful.")
                 return redirect('dashboard')  # Redirect to a home or dashboard page
             else:
                 messages.error(request, "Invalid credentials.")
         else:
             messages.error(request, "Please correct the errors below.")
     return render(request, 'events/loginadmin.html')

# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_superuser:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.error(request, "Invalid credentials or not an admin user.")
#     return render(request, 'events/loginadmin.html')