from django.shortcuts import render


def play_view(request):
    return render(request, 'Trainer/play.html')
