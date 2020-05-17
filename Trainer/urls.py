from django.urls import path
from . import views

app_name = 'Trainer'
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('play/', views.play_view, name='play'),
    path('statistics/', views.statistics_view, name='statistics')
]
