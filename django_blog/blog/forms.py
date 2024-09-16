from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget

# Extending the UserCreationForm for Registration
class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user        
    

class UserProfileForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['email', 'first_name', 'last_name']


class PostCreateForm(forms.ModelForm):
     title = forms.CharField(max_length=100)
     content = forms.Textarea()
     
     class Meta:
          model = Post
          fields = ['title', 'content', 'tags'] 
          widgets = {
            'tags': TagWidget(),
        }


class CommentForm(forms.ModelForm):
     class Meta:
          model = Comment
          fields = ['content']
          widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your comment here'}),
            }