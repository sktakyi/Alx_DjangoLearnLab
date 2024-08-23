from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username


from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth=None, profile_photo=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth=None, profile_photo=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, date_of_birth, profile_photo, password, **extra_fields)        


class MyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view", "Can view model"),
            ("can_create", "Can create model"),
            ("can_edit", "Can edit model"),
            ("can_delete", "Can delete model"),
        ]

  
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request, pk):
    # Logic for editing the model instance
    return render(request, 'edit_template.html')