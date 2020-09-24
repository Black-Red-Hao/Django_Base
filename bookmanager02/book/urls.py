from django.urls import path
from book.views import create_book

urlpatterns = [
    path('index/', create_book)
]