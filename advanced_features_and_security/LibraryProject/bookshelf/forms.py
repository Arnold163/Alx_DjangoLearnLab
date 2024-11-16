# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100, required=True)

    def clean_example_field(self):
        data = self.cleaned_data['example_field']
        
        # Example of sanitization or additional validation
        if "<script>" in data:
            raise forms.ValidationError("Invalid input - scripts are not allowed.")
        
        return data