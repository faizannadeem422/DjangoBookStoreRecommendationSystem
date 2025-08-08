from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title', 'book_author', 'book_publisher', 'book_price', 'category', 'book_content')

class UpdateBookForm(forms.ModelForm):
    book_title = forms.CharField(required=False)
    book_author = forms.CharField(required=False)
    book_publisher = forms.CharField(required=False)
    book_price = forms.IntegerField(required=False)
    category = forms.CharField(required=False)

    class Meta:
        model = Book
        fields = ('book_title', 'book_author', 'book_publisher', 'book_price', 'category')

