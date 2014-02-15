from django.http import Http404
from django.shortcuts import render

from cydoniaapp.models import Student
# Create your views here.

def index(request):
    context = {}
    return render(request, 'cydoniaapp/index.html', context)
