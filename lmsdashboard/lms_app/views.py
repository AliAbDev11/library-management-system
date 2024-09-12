from django.shortcuts import render
from .models import *

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    return render(request, 'pages/books.html')