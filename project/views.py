from django.shortcuts import render, redirect
from .models import *


def add_author(request):
    if request.method == 'POST':
        Author.objects.create(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            age=request.POST['age']
        )
        return redirect("create_book")
    author = Author.objects.all()
    return render(request, "create_author.html", {'author': author})



def update_author(request):
    if request.method == 'POST':
        firstname = Author.objects(firstname=firstname)



def add_book(request):
    if request.method == "POST":
        boook = request.POST
        book_f = request.FILES

        Books.objects.create(
            book_name=boook["book_name"], 
            caption=boook["caption"], 
            author = Books.objects.get(id=boook["author"]), 
            picture=book_f['picture']
        )
        return redirect("")
    book = Books.objects.all()
    return render(request, 'create_book.html', {'book':book})


def get_books(request):
    book=Books.objects.all()
    return render(request, 'show_book.html', {"book":book})



