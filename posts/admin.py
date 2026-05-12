# Import Django's built-in admin module
# This lets you manage your app (add/edit/delete data) through a web interface
from django.contrib import admin

# Import the Post model from your current app
# The dot (.) means "look in this app's models.py file"
from .models import Post, Status

# Register your models here.
# (Just a comment Django adds by default)

# This line makes the Post model visible in the admin panel
# After this, you can manage Posts at http://127.0.0.1:8000/admin/
admin.site.register([Post, Status])
    