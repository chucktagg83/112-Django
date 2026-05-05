# Import Django generic views for displaying data
# ListView = shows multiple objects (like a list of posts)
# DetailView = shows one object (like a single post)
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView

# Import your Post model (this connects your views to your database)
from .models import Post
from django.contrib.auth.models import User # Import User model to link posts to users


# Create your views here.

# -------------------------------
# LIST VIEW (shows all posts)
# -------------------------------
class PostListView(ListView):

    # Specifies which HTML template to use
    # Django will render this file when the view is accessed
    template_name = "posts/list.html"

    # Tells Django which model (table) to pull data from
    # This will automatically retrieve all Post objects
    model = Post

    # This is the name used in your HTML template
    # Default is "object_list", but we rename it to "posts"
    # So in HTML you can use: {% for post in posts %}
    context_object_name = "posts"
    

# -------------------------------
# DETAIL VIEW (shows one post)
# -------------------------------
class PostDetailView(DetailView):

    # Specifies which HTML template to use for a single post
    template_name = "posts/detail.html"

    # Tells Django which model to use
    # It will retrieve ONE Post based on the URL (usually by ID)
    model = Post

    # This is the name used in your template
    # Default is "object", but we rename it to "post"
    # So in HTML you can use: {{ post.title }}
    context_object_name = "single_post"


# -------------------------------
# CREATE VIEW (creates a new post)
# -------------------------------
class PostCreateView(CreateView):

    # Specifies which HTML template to use for the form
    template_name = "posts/new.html"

    # Tells Django which model to create an object for
    model = Post

    # Specifies which fields to show in the form
    # This will automatically generate form fields for title, subtitle, and body
    fields = ["title", "subtitle", "body"]
    
    def form_valid(self, form):
        # Before saving the form, set the author to the current logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

# -------------------------------
# UPDATE VIEW (updates one post)
# -------------------------------
class PostUpdateView(UpdateView):

    # Specifies which HTML template to use for the form
    template_name = "posts/edit.html"

    # Tells Django which model to update
    model = Post

    # Specifies which fields to show in the form
    fields = ["title", "subtitle", "body"]
    
# -------------------------------
# DELETE VIEW (deletes one post)
# -------------------------------
class PostDeleteView(DeleteView):

    # Specifies which HTML template to use for the delete confirmation
    template_name = "posts/delete.html"

    # Tells Django which model to delete an object from
    model = Post

    success_url = reverse_lazy("post_list") # reverse_lazy is used here because we need to wait until the URL patterns are loaded
    
    