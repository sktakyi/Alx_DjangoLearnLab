from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Retrieve all book objects from the database
    return render(request, 'book_list.html', {'books': books})

from django.shortcuts import render, redirect
from .forms import ExampleForm

def book_create(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'book_form.html', {'form': form})


