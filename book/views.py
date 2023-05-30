from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Book


def index(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, "book/index.html", context)

def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, "book/detail.html", {"book": book})