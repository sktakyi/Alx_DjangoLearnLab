from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# User Login
class UserLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True

# User Logout
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

# User Registration Form
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile Management
@login_required
def profile_view(request):
    return render(request, 'blog/profile.html')


# ListView for displaying all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Your template
    context_object_name = 'posts'  # Access posts in the template

# DetailView for displaying a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# CreateView for adding new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author as the logged-in user
        return super().form_valid(form)

# UpdateView for editing posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit

# DeleteView for deleting posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')  # Redirect after successful deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete
