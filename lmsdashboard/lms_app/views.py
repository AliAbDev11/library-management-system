from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        add_category = CategoryForm(request.POST)

        if add_book.is_valid():
            add_book.save()
            messages.success(request, "Book added successfully!")
        elif add_category.is_valid():
            add_category.save()
            messages.success(request, "Category added successfully!")
        else:
            messages.error(request, "There were errors in the form submission.")

        return redirect('index')  # Redirect after processing the POST request

    # Handle GET request
    add_book = BookForm()
    add_category = CategoryForm()
    books = Book.objects.all()

    context = {
        'categories': Category.objects.all(),
        'books': books,
        'form': add_book,
        'CategoryForm': add_category,
        'AllBooks': books.filter(active=True).count(),
        'SoldBooks': books.filter(status='sold').count(),
        'RentalBooks': books.filter(status='rental').count(),
        'AvailableBooks': books.filter(status='available').count(),
    }

    return render(request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    context = {
        'categories':Category.objects.all(),
        'CategoryForm':CategoryForm(),
        'books': search,
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