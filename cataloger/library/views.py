from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.
def bookdetail(request, book_id):
    if book_id:
        return HttpResponse(f"You are looking at Book {book_id}")
    else:
        return HttpResponse("No book selected")

def index(request):
    return render(request, 'index.html')