from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_view(request):
    context = {
        'signed_in': False,
        'curr_template': 'login',
        'form': UserCreationForm,
    }
    return render(request, 'Users/register.html', context)


def login_view(request):
    context = {
        'signed_in': False,
        'curr_template': 'login',
    }
    return render(request, 'Users/login.html', context)


def account_view(request):
    context = {
        'signed_in': True,
        'curr_template': 'account',
    }
    return render(request, 'Users/account.html', context)
