from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return []

# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return []

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        librarian = [Librarian.objects.get] (library__name=library_name)
        return librarian.name
    except Librarian.DoesNotExist:
        return None

# Example Usage
if __name__ == "__main__":
    print("Books by Author Name:", get_books_by_author("Author Name"))
    print("Books in Library Name:", get_books_in_library("Library Name"))
    print("Librarian for Library Name:", get_librarian_for_library("Library Name"))