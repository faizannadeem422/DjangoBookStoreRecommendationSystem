from django.urls import path
from .views import AddBook, DeleteBook, RecommendedBooks, ViewBook, FetchAllBooks, FetchBooksByCategory, UpdateBook, Home

urlpatterns = [
    # path('home/', Home, name='home'),
    path('add/', AddBook, name='add-book'),
    path('id/<int:bookId>/', ViewBook, name='view-book'),
    path('all', FetchAllBooks, name='fetch-all-books'),
    path('fetchbycategory/<str:category_p>/', FetchBooksByCategory, name='fetch-books-by-category'),
    path('update/<int:bookId>', UpdateBook, name='update-a-book'),
    path('delete/<int:bookId>', DeleteBook, name='delete-book'),

    path('recommended/', RecommendedBooks, name='recommended-books')
]