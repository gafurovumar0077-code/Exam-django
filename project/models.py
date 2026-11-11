from django.db import models
from datetime import *



class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    created_at = models.DateField(default=datetime.now())
    is_active = models.BooleanField(default=True)


class Books(models.Model):
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    caption = models.TextField()
    created_at = models.DateField(default=datetime.now())
    is_active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='images/')


class Order(models.Model):
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    get_at = models.DateField(default=datetime.now())
    bring_at = models.DateField(default=datetime.now())

    

    



























