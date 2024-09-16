# Authentication System Documentation

## Overview
- This authentication system allows users to register, log in, log out, and manage their profiles securely. It uses Django's built-in authentication system for login and logout, extends Django’s UserCreationForm for registration, and allows profile management for logged-in users.

## System Components:

- Views:
LoginView: Utilizes Django's built-in LoginView to authenticate users.
LogoutView: Uses Django’s LogoutView to log users out securely.
RegisterView: Extends Django’s UserCreationForm to handle user registration.
ProfileView: Allows users to view and update their profile details.

- Forms:
UserRegistrationForm: Extends Django’s UserCreationForm to include additional fields like email.
ProfileUpdateForm: A form to allow users to update their profile details.
Models:

- User Model: Django’s default User model is used for user authentication. You can extend this by creating a Profile model with additional fields (e.g., bio, profile picture).

- Templates:
Login Template: A form for users to input their username and password to log in.
Register Template: A form for users to input details like username, email, and password to register.
Profile Template: Displays user information and allows them to edit details.
User Interaction Flow
Registration:

- Users access the registration page at /register/.
They fill out the form, which includes fields for username, email, and password.
Upon successful registration, the user is automatically logged in and redirected to their profile or homepage.
Login:

- Users access the login page at /login/.
They input their username and password to log in.
If successful, they are redirected to their profile or a designated page. If not, an error message is displayed.
Logout:

- Users can log out by clicking a logout button that redirects to /logout/.
Upon logging out, they are redirected to a logged-out confirmation page or the homepage.
Profile Management:

- Authenticated users can view their profile at /profile/.
They can update details like their email, bio, or other profile-specific fields.
The form processes updates when submitted and provides feedback.

## Testing the Authentication Features

- Registration Test:
Go to the /register/ URL.
Fill out the form with a unique username, email, and password.
After submission, check if the user is redirected correctly and if the user is listed in the Django admin panel.

- Login Test:
Go to the /login/ URL.
Attempt to log in with the registered user credentials.
Ensure the user is redirected to their profile or the designated page.

- Logout Test:
After logging in, click the logout button or navigate to /logout/.
Ensure the user is logged out and redirected to the appropriate page.
Profile Management Test:

- Log in and go to the /profile/ URL.
Update user details like email or profile-specific fields.
Submit the form and ensure the changes reflect correctly in the user’s profile.

- Code Files
Views (blog/views.py):
Custom registration and profile views.
Import Django's built-in authentication views for login and logout.

-Forms (blog/forms.py):
UserRegistrationForm: Extends UserCreationForm.
ProfileUpdateForm: Handles profile updates.
Models (blog/models.py):
Extend the default User model by adding a Profile model if needed.

- Template Files
login.html: Contains the login form.
register.html: Contains the registration form.
profile.html: Displays user profile information and the profile update form.
Setup Instructions
Ensure Django's authentication views are properly included



# Django Blog Post Management

## Features

This application allows users to create, view, update, and delete blog posts. Authentication and permissions are required for certain actions.

### CRUD Operations:

1. **Post List**:
    - URL: `/posts/`
    - View: ListView
    - Shows all blog posts, ordered by the published date.

2. **Post Detail**:
    - URL: `/posts/<id>/`
    - View: DetailView
    - Displays full post content, author, and published date.

3. **Create Post**:
    - URL: `/post/new/`
    - View: CreateView
    - Only authenticated users can create new posts. The post author is automatically set to the logged-in user.

4. **Edit Post**:
    - URL: `/posts/<id>/edit/`
    - View: UpdateView
    - Only the post author can edit their own posts.

5. **Delete Post**:
    - URL: `/posts/<id>/delete/`
    - View: DeleteView
    - Only the post author can delete their own posts.

### Permissions

- **Create Posts**: Only authenticated users can create posts.
- **Edit/Delete Posts**: Only the post author can edit or delete their own posts.
- **View Posts**: Any user (authenticated or not) can view the list and detail of blog posts.

### Testing

1. **Test post creation, editing, and deletion** as both the post author and as a different user.
2. **Ensure form validation** works as expected, and error messages are shown for invalid inputs.
3. **Verify permissions** for unauthenticated users (ensure they are redirected to the login page).
4. **Test security**: Ensure all forms are protected using CSRF tokens.
5. **Navigation**: Check that users are redirected to the correct views after creating, editing, or deleting posts.

## Setup Instructions

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Apply migrations:
    ```bash
    python manage.py migrate
    ```
4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Notes

- This application uses Django’s built-in `LoginRequiredMixin` and `UserPassesTestMixin` to manage permissions for post creation, editing, and deletion.