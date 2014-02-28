from django.forms import ModelForm
from booker.models import Customer, Book

class CustomerForm(ModelForm):
    class Meta:
        model = Customer

class BookForm(ModelForm):
	class Meta:
		model = Book
