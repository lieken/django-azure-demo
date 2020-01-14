# house/views.py
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'house/index.html', context=None)
