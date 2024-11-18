from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, AdminRegistrationForm
from .models import Registrant
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
import logging
logger = logging.getLogger('events')
logger = logging.getLogger(__name__)



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            interest = form.cleaned_data['interest']

            # Check if email already exists
            if Registrant.objects.filter(email=email).exists():
                message = f"The email {email} is already registered. Please use a different email."
                messages.error(request, message)
                logger.warning(f"Registration failed for {name} - {message}")
            else:
                try:
                    # Save the data to the Registrant model
                    Registrant.objects.create(
                        name=name,
                        email=email,
                        interest=interest
                    )
                    success_message = f"Thank you, {name}! You have successfully registered for the event."
                    messages.success(request, success_message)
                    logger.info(f"New registration: {name} ({email}) - Interest: {interest}")
                    return render(request, 'events/register.html')
                except Exception as e:
                    error_message = logger.error(f"Error during registration for {email}: {str(e)}")
                    messages.error(request, error_message)
                    logger.error(f"Error during registration for {email}: {str(e)}")
        else:
            # Log and show specific form validation errors
            error_details = form.errors.as_json()
            logger.error(f"Registration form validation failed: {error_details}")
            # error_exact=error_details
            # messages.error(request, "Form submission failed. Please fix the errors below and try again.")
    
    # Render the form with any error messages and pre-filled data if available
    form = RegistrationForm()
    return render(request, 'events/register.html', {'form': form})


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



def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)  # Log in the newly registered admin
                logger.info("New admin registered: Username: %s, Email: %s", user.username, user.email)
                messages.success(request, "Admin registered successfully!")
                return redirect('admin-login')  # Redirect to dashboard
            except Exception as e:
                logger.error(f"Unexpected error during admin registration: {str(e)}")
                messages.error(request, "An unexpected error occurred. Please try again.")
        else:
            # Log the specific errors
            logger.error("Admin registration failed. Errors: %s", form.errors.as_json())

            # Extract error messages for user feedback
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = AdminRegistrationForm()

    return render(request, 'events/adminregister.html', {'form': form})

def csrf_failure(request, reason=""):
    return HttpResponse("CSRF verification failed. Please reload the page and try again.", status=403)

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