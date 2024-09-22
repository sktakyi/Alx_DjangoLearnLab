from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Post Model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments')
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'


# Like Model
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_by' ) 
    
    # Ensures a user can like a post only once
    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user} liked {self.post}"
