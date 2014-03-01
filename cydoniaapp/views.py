from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from cydoniaapp.models import Student
# Create your views here.

def index(request):
    context = {}
    return render(request, 'cydoniaapp/index.html', context)

@login_required
def profile(request):
    context = {}
    return render(request, 'cydoniaapp/profile.html', context)

