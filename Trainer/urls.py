from django.urls import path
from . import views

app_name = 'Trainer'
urlpatterns = [
    path('play/', views.play_view, name='play'),
]
