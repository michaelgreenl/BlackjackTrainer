from django.urls import path
from . import views

app_name = 'BlackjackGame'
urlpatterns = [
    path('play/', views.play_view, name='play'),
]
