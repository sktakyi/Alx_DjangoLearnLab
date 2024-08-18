from bookshelf.models import Book

# Create
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Retrieve
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Update
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# Delete
book.delete()
print(Book.objects.all())