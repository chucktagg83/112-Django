# Import the path function used to define URL routes
from django.urls import path

# Import the views we want to connect to URLs
# The dot (.) means "from this same folder (posts app)"
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView # Import PostUpdateView and PostDeleteView for editing and deleting posts]


# This list tells Django:
# "When a user visits a specific URL, run this view"
urlpatterns = [

    # "" = homepage (root URL for this app)
    # Example: http://127.0.0.1:8000/posts/  (if included in main urls)
    # This will display a list of all posts
    path("", PostListView.as_view(), name="post_list"),
    # PostListView.as_view() converts the class into a callable view
    # name="post_list" allows us to reference this URL in templates


    # "posts/<int:pk>/" = dynamic URL pattern
    # Example: http://127.0.0.1:8000/posts/1/
    #
    # <int:pk> means:
    #   - int → only numbers are allowed
    #   - pk → primary key (ID of the post in the database)
    #
    # Django automatically passes this value to the view
    # so it knows WHICH post to display

    # This will display ONE specific post based on its ID
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    # PostDetailView will retrieve a single Post object using the pk
    # name="post_detail" is used in templates like:
    # {% url 'post_detail' post.id %}


    # "posts/create/" = URL for creating a new post
    # Example: http://127.0.0.1:8000/posts/create/
    #
    # This route loads a form where the user can enter post data

    path("posts/create/", PostCreateView.as_view(), name="post_new"),
    # PostCreateView handles:
    #   - displaying the form (GET request)
    #   - saving the form data (POST request)
    #
    # name="post_new" allows usage in templates like:
    # {% url 'post_new' %}
    
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"), # URL for editing an existing post
    # Example: http://127.0.0.1:8000/posts/1/edit/
    # PostUpdateView handles:
    #   - displaying the form with existing data (GET request)
    #   - saving the updated data (POST request)
    # name="post_edit" allows usage in templates like:
    # {% url 'post_edit' post.id %}
    
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"), # URL for deleting a post
    # Example: http://127.0.0.1:8000/posts/1/delete/
    # PostDeleteView handles:
    #   - confirming deletion (GET request)
    #   - deleting the post (POST request)
    # name="post_delete" allows usage in templates like:    
    # {% url 'post_delete' post.id %}
]