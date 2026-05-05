# Import Django's database model tools (used to create tables/fields)
from django.db import models

# Import Django's built-in User model (for linking posts to users)
from django.contrib.auth import get_user_model

# Import reverse() to dynamically create URLs (instead of hardcoding)
from django.urls import reverse


# Create your Post model (this becomes a database table)
class Post(models.Model):

    # Title of the post (short text, max 128 characters)
    title = models.CharField(max_length=128)

    # Subtitle of the post (short text, max 256 characters)
    subtitle = models.CharField(max_length=256)

    # Main content of the post (long text, no limit)
    body = models.TextField()

    # Automatically stores the date/time when the post is created
    created_on = models.DateTimeField(auto_now_add=True)

    # Links each post to a user (author)
    # ForeignKey = relationship to another table (User table)
    # CASCADE = if user is deleted, their posts are deleted too
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    # Controls how the post appears in Django Admin (string format)
    def __str__(self):
        # Example output: "1 - My Post Title by admin"
        return f"{self.id} - {self.title} by {self.author}"

    # Returns the URL for this specific post
    def get_absolute_url(self):
        # reverse() looks for a URL named "post_detail"
        # and passes the post ID into it
        return reverse("post_detail", args=[self.id])