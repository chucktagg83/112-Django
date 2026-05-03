# Import ListView (used to display a list of objects)
from django.views.generic import ListView

# Import your Post model
from .models import Post


# Create your views here.

# Create a class-based view to display a list of posts
class PostListView(ListView):

    # This tells Django which HTML file to use
    template_name = "posts/list.html"

    # This tells Django what data to pull from the database
    model = Post

    # This is the name used in your template (HTML)
    # Instead of "object_list", you can use "posts"
    context_object_name = "posts"