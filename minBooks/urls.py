from django.urls import path 
from .views import index ,get_single_book ,get_auther,edit_book,delete_book, add_book


urlpatterns = [
    path('', index),
    path('new', add_book,name="add_book"),
    path('<int:book_id>', get_single_book ,name="book_details" ),
    path('edit/<int:book_id>', edit_book ,name="edit_book" ),
    path('delete/<int:book_id>', delete_book ,name="delete_book" ),
    path('auther/<int:auther_id>', get_auther)
]
