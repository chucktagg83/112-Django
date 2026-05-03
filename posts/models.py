from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128) # string
    subtitle = models.CharField(max_length=256) # string
    body = models.TextField()# string
    created_on = models.DateTimeField(auto_now_add=True)# data/datetime
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)  # User Model (ForeignKey)
    
    def __str__(self): # to return a string representation of the Post object
        return f"{self.id} - {self.title} by {self.author}" # This will show the title of the post in the admin panel instead of "Post object (1)", "Post object (2)", etc.

    def get_absolute_url(self): # to return a string representation of the Post object
        return reverse("post_detail", args=[self.id]) # This will show the title of the post in the admin panel instead of "Post object (1)", "Post object (2)", etc.