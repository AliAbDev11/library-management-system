from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'book_img':forms.FileInput(attrs={'class':'form-control'}),
            'author_img':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_bookprice':forms.NumberInput(attrs={'class':'form-control', 'id':'rentalprice'}),
            'retal_period':forms.NumberInput(attrs={'class':'form-control', 'id':'rentaldays'}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control', 'id':'totalrental'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }