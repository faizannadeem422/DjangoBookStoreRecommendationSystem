from django.db import models
from django.contrib.auth.models import User

defaultBookContent = """ 
    Here's a detailed explanation of the Django Authentication System, covering all the points you've listed:

    🔐 Django Authentication System
    Django comes with a built-in authentication system that handles:

    User registration and login

    Password hashing and security

    Permissions and groups

    Custom user models

    Lets explore each part in detail:

    1. ✅ User Model & User Management
    Django provides a built-in User model in django.contrib.auth.models.

    Default fields:

    username

    password (stored hashed)

    email

    first_name, last_name

    is_active, is_staff, is_superuser

    last_login, date_joined
"""

class Book(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200, null=True, blank=True)
    book_publisher = models.CharField(max_length=200, null=True, blank=True)
    book_price = models.IntegerField()
    category = models.CharField(max_length=255)
    book_content = models.TextField(default=defaultBookContent)

    def __str__(self):
        return f"{self.book_title} by {self.book_author or 'Unknown'}"


class BookOpenFrequency(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    frequency = models.IntegerField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.book.book_title} opened {self.frequency} times"
