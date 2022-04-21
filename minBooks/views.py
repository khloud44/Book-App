import json
from msilib import CreateRecord
from msilib.schema import ListView
import os.path
import pdb

from django.conf import settings
from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse
from minBooks.form import BookForm

from minBooks.models import Book ,Author


# Create your views here.

def index(request):
    books=Book.objects.all()
    context={
        "books":books
    }
    return render(request, "minBooks/index.html",context=context)   
    # Path as i sande at tempaltes


def get_single_book(request , book_id):
    book =Book.objects.get(id=book_id)
    book_img = os.path.basename(book.image.url)
    author=Author.objects.get(id=book.author.id)
    context ={
        "book" : book,
        "image":book_img,
        "author":author
        }
    return render(request , "minBooks/book_details.html" , context=context)   


def get_auther(request,auther_id):
    authorBook=Author.objects.get(id=auther_id)
    books=Book.objects.filter(author=auther_id)
    context ={
        "author":authorBook,
        "books":books
        }  
    return render(request , "minBooks/auther_details.html" , context=context)

#----------------------------------------------#

def add_book(request):
    if request.method =="POST":
        form=BookForm(request.POST , request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect("book_details" , book_id=book.id)
    else:
        form = BookForm()
    return render(request , "minBooks/form.html" , context={"form": form})    


def edit_book(request,book_id):
    book= get_object_or_404(Book,id=book_id)
    if request.method =="POST":
        form=BookForm(request.POST , request.FILES , instance=book)
        if form.is_valid():
            book = form.save()
            return redirect("book_details" , book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, "minBooks/form.html",context={"form": form})

def delete_book(request,book_id):
    Book.objects.filter(id=book_id).delete()
    books=Book.objects.all()
    context={
        "books":books
    }
    return render(request, "minBooks/index.html",context=context) 
