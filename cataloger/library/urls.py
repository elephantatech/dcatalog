from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:book_id>', views.bookdetail, name="book" ),
    path('', views.index, name='index')
]
