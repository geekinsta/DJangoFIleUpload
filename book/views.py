from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    context = {}
    context['books'] = Book.objects.all()
    return render(request, 'book/home.html', context)

def create_book(request):
    if request.method == 'GET':
        context = {'form': BookForm()}
        return render(request, 'book/create.html', context)

    elif request.method == 'POST':

        # Passing uploaded files as request.files
        form = BookForm(request.POST, request.FILES)

        # Validating and saving the form
        if form.is_valid():
            form.save()
            return redirect('book_home')
        else:
            context = {'form': form}
            return render(request, 'book/create.html', context)