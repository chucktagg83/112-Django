# Import Django generic views for displaying data
# ListView = shows multiple objects (like a list of posts)
# DetailView = shows one object (like a single post)
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView

from posts import apps

# Import your Post model (this connects your views to your database)
from .models import Post, Status
from django.contrib.auth.models import User # Import User model to link posts to users
from django.urls import reverse_lazy # Import reverse_lazy for redirecting after delete
from django.contrib.auth.mixins import (
    LoginRequiredMixin, # Import LoginRequiredMixin to restrict access to certain views
    UserPassesTestMixin, # Import UserPassesTestMixin to restrict access to certain views based on custom logic
    ) 

# Create your views here.

# -------------------------------
# LIST VIEW (shows all posts)
# -------------------------------
class PostListView(ListView):
    
    template_name = "posts/list.html" 
    # This tells Django to use the "list.html" template when rendering this view. By default, it would look for "post_list.html" based on the model name, but we specify it explicitly here.
    
    model = Post 
    # This tells Django which model to use for this view. It will automatically retrieve all Post
    
    context_object_name = "posts" 
    # This changes the default context variable name from "object_list" to "posts". In your template, you can now use {% for post in posts %} instead of {% for post in object_list %}.       


def get_queryset(self):
    # This method allows you to customize the queryset that is used to retrieve objects for this view.
    # In this example, we filter the posts to only show those with the "Published" status and order them by creation date (newest first).
    return Post.objects.filter(status=published_status).order_by("-created_on")

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(f"Before modifying context: \n{context}") # Print the original context for debugging
    context["new_elements"] = "This is some new data added to the context!" # Add new data to the context  
    print(f"After modifying context: \n{context}") # Print the modified context for debugging   
    return context
# This method allows you to add extra data to the context that is passed to the template.
# In this example, we just print the context to the console for debugging purposes.   

# -------------------------------
# DETAIL VIEW (shows one post)
# -------------------------------
class PostDetailView(LoginRequiredMixin, DetailView):

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
class PostCreateView(LoginRequiredMixin,CreateView):

    # Specifies which HTML template to use for the form
    template_name = "posts/new.html"

    # Tells Django which model to create an object for
    model = Post

    # Specifies which fields to show in the form
    # This will automatically generate form fields for title, subtitle, and body, status but not for author (we will set that in form_valid)
    fields = ["title", "subtitle", "body", "status"]
    
    def form_valid(self, form):
        # Before saving the form, set the author to the current logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

# -------------------------------
# UPDATE VIEW (updates one post)
# -------------------------------
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    # Specifies which HTML template to use for the form
    template_name = "posts/edit.html"

    # Tells Django which model to update
    model = Post

    # Specifies which fields to show in the form
    fields = ["title", "subtitle", "body", "status"]
    
    
    def test_func(self):
        # Get the post object that is being updated
        post = self.get_object()
        
        if self.request.user.is_authenticated: # Check if the user is logged in
        # Check if the current logged-in user is the author of the post
            if self.request.user == post.author:
                return True # Allow access to update if user is the author
        else:
            return False # Deny access if user is not the author
# DELETE VIEW (deletes one post)
# -------------------------------
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    # Specifies which HTML template to use for the delete confirmation
    template_name = "posts/delete.html"

    # Tells Django which model to delete an object from
    model = Post

    success_url = reverse_lazy("post_list") # reverse_lazy is used here because we need to wait until the URL patterns are loaded
    
    def test_func(self):
        # Get the post object that is being updated
        post = self.get_object()
        
        if self.request.user.is_authenticated: # Check if the user is logged in
        # Check if the current logged-in user is the author of the post
            if self.request.user == post.author:
                return True # Allow access to update if user is the author
        else:
            return False # Deny access if user is not the author
        
# POSTARCHIVEDLISTVIEW (shows all archived posts)
# -------------------------------

class PostArchivedListView(ListView):
    template_name = "posts/list.html" 
    archived_status = Status.objects.get(name="Archived") # Get the Status object for "Archived" status
    queryset = Post.objects.filter(status=archived_status)
    context_object_name = "posts"
    
# POSTDraftListView (shows all draft posts)
# -------------------------------

class PostDraftListView(ListView):
    template_name = "posts/list.html" 
    draft_status = Status.objects.get(name="Draft") # Get the Status object for "Draft" status
    queryset = Post.objects.filter(status=draft_status)
    context_object_name = "posts"