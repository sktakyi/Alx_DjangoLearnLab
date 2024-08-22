from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
def Books_By_Author(author_name):
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    
    print("All Books by the author:")
    for book in books_by_author:
        print(book.title)

# List all books in a library.
def Books_in_Library(library_name):
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    
    print("All Books in the Library")
    for book in books_in_library:
        print(book.title)

# Retrieve the librarian for a library.
def Librarian_for_Library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)

    print(f"The Librarian for the library is: {librarian.name}")