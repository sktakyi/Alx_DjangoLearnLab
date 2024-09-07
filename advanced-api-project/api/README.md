## API Endpoints

- `/books/`: Lists all books (GET) and allows authenticated users to create a new book (POST).
- `/books/<int:pk>/`: Allows retrieving (GET), updating (PUT/PATCH), or deleting (DELETE) a book by ID.

## Permissions
- `IsAuthenticatedOrReadOnly`: Unauthenticated users can view data (GET), but only authenticated users can create, update, or delete data (POST/PUT/DELETE).

## Testing Strategy

This document outlines the approach for testing the API endpoints in the `advanced_api_project`.

### Test Cases

1. **CRUD Operations**
   - **Create Book:** Tests if a new book can be created.
   - **Read Book:** Tests if book details can be retrieved.
   - **Update Book:** Tests if a book can be updated.
   - **Delete Book:** Tests if a book can be deleted.

2. **Functionality Tests**
   - **Filtering:** Tests if filtering by title works.
   - **Searching:** Tests if searching by title returns correct results.
   - **Ordering:** Tests if ordering by publication year works.

### Running Tests

Run tests with:
```bash
python manage.py test api
