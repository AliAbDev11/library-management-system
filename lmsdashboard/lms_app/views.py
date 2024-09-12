from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'pages/index.html')

def books(request):
    return render(request, 'pages/books.html')