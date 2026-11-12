from django.shortcuts import render, redirect
from .models import Author, Books, Order


def home(request):
    return render(request, 'home.html')


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

def see_author(request):
    author = Author.objects.all()
    return render(request, 'see_author.html', {'author': author})

def update_author(request, id):
    author = Author.objects.get(pk=id)
    if request.method == "POST":
        author.firstname = request.POST["firstname"]
        author.lastname = request.POST["lastname"]
        author.age = request.POST["age"]
        author.save()
        return redirect('see_author')
    return render(request, 'update_author.html', {'author': author})


def delete_author(request, id):
    author = Author.objects.get(pk=id)
    author.delete()
    return redirect('home')







def add_book(request):
    if request.method == "POST":
        boook = request.POST
        book_f = request.FILES
        Books.objects.create(
            book_name=boook["book_name"],
            caption=boook["caption"],
            autor=Author.objects.get(id=boook["autor"]),
            picture=book_f['picture']
        )
        return redirect("show_book")
    book = Books.objects.all()
    return render(request, 'create_book.html', {'book': book, 'author': Author.objects.all()})


def get_books(request):
    book=Books.objects.all()
    return render(request, 'show_book.html', {"book":book})



def update_books(request, id):
    books = Books.objects.get(pk=id)
    if request.method == "POST":
        books.autor_id = request.POST['autor']
        books.book_name = request.POST['book_name']
        books.caption = request.POST['caption']
        books.picture = request.FILES['picture']
        books.save()
        return redirect('show_book')
    return render(request, 'update_books.html', {'books': books,'author': Author.objects.all()})


def delete_books(request, id):
    book = Books.objects.get(pk=id)
    book.delete()
    return redirect('home')



def create_order(request):
    if request.method == "POST":
        Order.objects.create(
            username=request.POST["username"],
            phone=request.POST["phone"],
            books=Books.objects.get(pk=request.POST["books"]),
            get_at=request.POST["get_at"],
            bring_at=request.POST["bring_at"]
            )
        return redirect('see_order')
    return render(request, 'create_order.html', {'books': Books.objects.all()})



def see_order(request):
    orders = Order.objects.all()
    return render(request, 'see_orders.html', {'orders': orders})



def update_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.username = request.POST['username']
        order.phone = request.POST['phone']
        order.books = Books.objects.get(pk=request.POST['books'])
        order.get_at = request.POST['get_at']
        order.bring_at = request.POST['bring_at']
        order.save()
        return redirect('see_order')
    return render(request, 'update_order.html', {'order': order,'books': Books.objects.all()})



def delete_order(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('home')
