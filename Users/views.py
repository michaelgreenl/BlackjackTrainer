from django.shortcuts import render, redirect
from Users.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('Users:account')

    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}'.format(username))
            return redirect('Users:login')
    else:
        register_form = UserRegistrationForm()

    context = {
        'title': 'Register',
        'register_form': register_form,
    }
    return render(request, 'Users/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('Users:account')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully signed in as {}'.format(username))
            return redirect('Trainer:play')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {
        'title': 'Login',
    }
    return render(request, 'Users/login.html', context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('Users:login')


@login_required(login_url='login')
def account_view(request):
    context = {
        'title': 'Account',
        'signed_in': True,
    }
    return render(request, 'Users/account.html', context)
