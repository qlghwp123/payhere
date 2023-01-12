from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as auth_login, 
    logout as auth_logout
)
from .forms import CustomUserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            return redirect('articles:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/sign.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            return redirect('articles:index')

    else:
        form = AuthenticationForm(request)

    context = {
        'form': form
    }

    return render(request, 'accounts/sign.html', context)


@login_required
def logout(request):
    auth_logout(request)

    return redirect('accounts:login')