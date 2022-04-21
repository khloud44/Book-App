from django import forms

from minBooks.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=" __all__"
        fields=["name" ,"description" ,"image" ,"price","published_at","appropriate_to","author"]