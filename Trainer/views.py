from django.shortcuts import render


def home_view(request):
    context = {
        'signed_in': signed_in_check(),
    }
    return render(request, 'Trainer/home.html', context)


def play_view(request):
    context = {
        'signed_in': signed_in_check(),
        'curr_template': 'play',
    }
    return render(request, 'Trainer/play.html', context)


def statistics_view(request):
    context = {
        'signed_in': signed_in_check(),
        'curr_template': 'statistics',
    }


def signed_in_check():
    # TODO: Add check for if the user is signed in
    return True
