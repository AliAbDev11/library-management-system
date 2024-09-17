from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
    context = {
        'categories':Category.objects.all(),
        'books': Book.objects.all(),
        'form':BookForm(),
        'CategoryForm':CategoryForm(),
        'AllBooks':Book.objects.filter(active=True).count(),
        'SoldBooks':Book.objects.filter(status='sold').count(),
        'RentalBooks':Book.objects.filter(status='rental').count(),
        'AvailableBooks':Book.objects.filter(status='available').count(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'categories':Category.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES, instance=book_id)
        if book_form.is_valid():
            book_form.save()
            return redirect('/')
    else:
        book_form = BookForm(instance=book_id)
    context = {
        'bookForm': book_form,
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')