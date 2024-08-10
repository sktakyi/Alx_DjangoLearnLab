from django.contrib import admin
from .models import Book

# Register the Book model with custom configurations
class BookAdmin(admin.ModelAdmin):
    # Customizing the admin display
    list_display = ('title', 'author', 'publication_year')
    
    # Adding search functionality
    search_fields = ('title', 'author')
    
    # Adding filters to the admin interface
    list_filter = ('publication_year',)

# Registering the model and admin customization
admin.site.register(Book, BookAdmin)