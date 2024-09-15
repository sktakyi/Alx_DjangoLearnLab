from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
