from unicodedata import category
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from bookstore.models import Book, BookOpenFrequency
from .forms import CustomUserCreationForm, AddBookForm, UpdateBookForm

# Home route
@login_required
def Home(request):
    return render(request, 'home.html')

# Register a new user
def RegisterNewUser(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# This will log the user out
def logout_view(request):
    logout(request)
    return redirect('login')

# Add a new book
@login_required
def AddBook(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            print(request.user)
            book.save()
            return redirect('fetch-all-books')
    else:
        form = AddBookForm()
    return render(request, 'addbook.html', {'form': form})

# Fetch a single book
@login_required
def ViewBook(request, bookId):
    book = get_object_or_404(Book, id=bookId)

    try:
        bookFrequency = BookOpenFrequency.objects.get(
            category = book.category
        )

        bookFrequency.frequency += 1
        bookFrequency.save()
    except:
        BookOpenFrequency.objects.create(
            frequency = 1,
            category = book.category
        )

    return render(request, 'viewbook.html', {'book': book})

# Fetch all books
@login_required
def FetchAllBooks(request):
    books = Book.objects.all()
    return render(request, 'allbooks.html', {'books': books})

# Fetch book by specific category
@login_required
def FetchBooksByCategory(request, category_p):
    books = Book.objects.filter(category=category_p)
    return render(request, 'allbooks.html', {'books' : books})

# Update a book
@login_required
def UpdateBook(request, bookId:int):
    book = get_object_or_404(Book, pk=bookId)

    if request.method == 'POST':
        form = UpdateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('fetch-all-books')  # or your success URL
    else:
        form = UpdateBookForm(instance=book)

    return render(request, 'updatebook.html', {'form': form})

# Delete a book
@login_required
def DeleteBook(request, bookId:int):
    book = get_object_or_404(Book,pk=bookId)

    if request.method == 'POST':
        book.delete()
        return redirect('fetch-all-books')
    
    return render(request, 'confirmdelete.html', {'book': book})

# Recommended Books
@login_required
def RecommendedBooks(request):
    frequencies = BookOpenFrequency.objects.all().order_by('-frequency')[:4]

    books = []
    for frequency in frequencies:
        books_ = Book.objects.filter(category__iexact=frequency.category)[:10]
        books.extend(books_)

    return render(request, 'allbooks.html', {'books': books})