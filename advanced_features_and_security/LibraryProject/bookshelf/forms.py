from django.views.decorators.csrf import csrf_protect
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