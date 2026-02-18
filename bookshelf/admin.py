from django.contrib import admin
from bookshelf.models import Book, Category, Author

# Register your models here.
admin.site.register(Category)
admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'year', 'category']
    list_display_links = ['title']
    search_fields = ['title', 'category']
    list_per_page = 5
