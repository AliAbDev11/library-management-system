from django.urls import path
from . import views

urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
]