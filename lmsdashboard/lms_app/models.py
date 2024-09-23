from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    status_book = [
        ('available', 'available'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)  # Increased max_length for flexibility
    book_img = models.ImageField(upload_to='photo', null=True, blank=True)
    author_img = models.ImageField(upload_to='photo', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True, default=0)  # Set default
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    rental_bookprice = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    rental_period = models.IntegerField(null=True, blank=True, default=0)  # Corrected typo from 'retal'
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.rental_bookprice and self.rental_period:
            self.total_rental = self.rental_bookprice * self.rental_period
        super(Book, self).save(*args, **kwargs)