from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
    return render(request, 'bookshelf/index.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'bookshelf/categories.html', {'categories' : categories})

def category(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    books = category.book_set.all()
    context = {
        'category' : category,
        'books' : books
    }
    return render(request, 'bookshelf/category.html', context)