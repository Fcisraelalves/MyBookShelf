from django.shortcuts import render
from .models import Category
# Create your views here.
def index(request):
    return render(request, 'bookshelf/index.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'bookshelf/categories.html', {'categories' : categories})