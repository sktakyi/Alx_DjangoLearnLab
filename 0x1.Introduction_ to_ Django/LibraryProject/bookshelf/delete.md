# Delete Operation
from bookshelf.models import Book

# Find the book by title
book = Book.objects.get(title="Your Book Title")

# Delete the book
book.delete()

**Command:**
```python
book.delete()
print(Book.objects.all())

# Expected output
<QuerySet []>