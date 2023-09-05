from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from Doctors.models import Doctor


def register(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request, user)
        return redirect('home')
    return render(request, 'accounts/register.html', {'forms': forms})


def profile(request):

    return render(request, 'profile.html')


def user_login(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        login(request, user)
        return redirect('homepage')
    return render(request, 'accounts/signin.html')


def user_logout(request):
    logout(request)

    return redirect('login')
