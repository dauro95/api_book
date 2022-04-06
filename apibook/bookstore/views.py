
# Create your views here.

from django.shortcuts import render

from rest_framework import viewsets

from .serializers import BookSerializer,AuthorSerializer
from .models import Author,Book

class AuthorViewSet (viewsets.ModelViewSet):
    
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer


class BookViewSet (viewsets.ModelViewSet):
    
    queryset=Book.objects.all()
    serializer_class=BookSerializer