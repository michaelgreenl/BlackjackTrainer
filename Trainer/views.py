from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def play_view(request):
    context = {
        'title': 'Play',
        'signed_in': request.user.is_authenticated
    }
    return render(request, 'Trainer/play.html', context)


@login_required(login_url='login')
def statistics_view(request):
    context = {
        'title': 'Statistics',
        'signed_in': request.user.is_authenticated,
    }
    return render(request, 'Trainer/statistics.html', context)
