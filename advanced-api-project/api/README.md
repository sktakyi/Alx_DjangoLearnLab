## API Endpoints

- `/books/`: Lists all books (GET) and allows authenticated users to create a new book (POST).
- `/books/<int:pk>/`: Allows retrieving (GET), updating (PUT/PATCH), or deleting (DELETE) a book by ID.

## Permissions
- `IsAuthenticatedOrReadOnly`: Unauthenticated users can view data (GET), but only authenticated users can create, update, or delete data (POST/PUT/DELETE).