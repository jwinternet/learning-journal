"""Defines URL patterns for learning_journals."""

from django.urls import path

from . import views

app_name = 'learning_journals'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
