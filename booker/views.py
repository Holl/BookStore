from django.shortcuts import render_to_response, render, redirect
import requests
from bottle import request, route, run
from django.http import HttpResponse
from booker.models import Customer, Book 
from booker.forms import CustomerForm, BookForm

def home(request):

	return render(request, "home.html")

def new_book(request):

	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			if form.save():
				return redirect("/show_books")
	else:
		form = BookForm()
	data = {
		"book_form" : form
		} 
	return render(request, "new_book.html", data)

def show_books(request):

	dataums= Book.objects.all()
	datos = Customer.objects.all()

	polls = {"books": dataums, "customers": datos}

	response = render_to_response(
		"show_books.html",
		polls
		)

	return response

def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    data = {"book": book}
    return render(request, "show_book.html", data)

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            if form.save():
                return redirect("/show_books/")
    else:
        form = BookForm()
    data = {"book": book, "book_form": form}
    return render(request, "edit_book.html", data)

def add_owner(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/show_books/")
    else:
        form = CustomerForm()
    data = {"customer_form": form}
    return render(request, "add_owner.html", data)

def show_customers(request):
	dataums= Book.objects.all()
	datos = Customer.objects.all()

	data = {"books": dataums, "customers": datos}

	return render(request, "show_customers.html", data)

