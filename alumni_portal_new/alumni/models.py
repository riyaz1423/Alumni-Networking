from django.db import models
from django.contrib.auth.models import User

class Alumni(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)  # Add email field
    password = models.CharField(max_length=255)  # Store hashed password
    batch = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.title} - {self.date}"
    
class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Alumni user
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to alumni user
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
