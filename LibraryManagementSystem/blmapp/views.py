from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import book

# Create your views here.
def homepageview(request):
    books = book.objects.all()
    return render(request, "homepage.html", {'books':books})

def addbookview(request):
    return render(request, "addbooks.html")

def addbook(request):
    if request.method == 'POST':
        book_title = request.POST['title']
        book_price = request.POST['price']
        curr_book = book()
        curr_book.title = book_title
        curr_book.leaseCost = book_price
        curr_book.save()
        return HttpResponseRedirect('/')

def editbookview(request):
    return render(request, "addbooks.html")

def editbook(request):
    return render(request, "addbooks.html")
