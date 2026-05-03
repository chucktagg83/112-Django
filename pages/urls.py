# Import the 'path' function from Django
# This is used to create URL routes (webpage addresses)
from django.urls import path

# Import views from the current folder (the dot means "this app")
# These are the functions/classes that control what each page shows
from .views import (
    HomePageView,      # Class-based view for the home page
    AboutPageView,     # Class-based view for the about page
    contact_me         # Function-based view for the contact page
)

# This list holds all the URL routes for this app
urlpatterns = [

    # "" means the root URL (homepage)
    # HomePageView.as_view() converts the class into something Django can use
    # name="home" lets you refer to this URL in templates (like links)
    path("", HomePageView.as_view(), name="home"),

    # "about/" means http://your-site.com/about/
    # AboutPageView.as_view() loads the About page
    path("about/", AboutPageView.as_view(), name="about"),

    # "contact/" means http://your-site.com/contact/
    # contact_me is a function (not a class), so no .as_view() needed
    path("contact/", contact_me, name="contact"),    
]