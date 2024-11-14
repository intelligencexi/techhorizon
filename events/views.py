from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import Registrant
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView





def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the data to the Registrant model
            Registrant.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                interest=form.cleaned_data['interest']
            )
            messages.success(request, "Registration successful.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    return render(request, 'events/register.html')

def login(request):
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

class AdminOnlyView(UserPassesTestMixin, TemplateView):
    template_name = 'events/admin_only.html'

    def test_func(self):
        return self.request.user.is_superuser