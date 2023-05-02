from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='hello'),
    path('bot/', views.bot_test, name='bot_testing'),
]