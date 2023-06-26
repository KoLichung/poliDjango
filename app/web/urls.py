from django.urls import path, include
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('process_price', views.process_price, name='process_price'),
    path('types', views.types, name='types'),
    path('featured_case', views.featured_case, name='featured_case'),
    path('q_and_a', views.q_and_a, name='q_and_a'),
    path('contact', views.contact, name='contact'),
]