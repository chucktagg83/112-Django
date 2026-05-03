# Import 'render' shortcut
# This helps you load an HTML template and send it to the browser
from django.shortcuts import render

# Import TemplateView (a built-in class for simple pages)
# Useful when you just want to show an HTML file
from django.views.generic import TemplateView

# Import HttpResponse (used to send simple text responses)
from django.http import HttpResponse

# Create your views here.
# (Just a comment Django adds for organization)

# ------------------ CLASS-BASED VIEWS ------------------

# Create a class for the Home page
class HomePageView(TemplateView):
    
    # Tell Django which HTML file to use for this page
    template_name = "pages/home.html"
    

# Create a class for the About page
class AboutPageView(TemplateView):
    
    # This connects the About page to its HTML template
    template_name = "pages/about.html"


# ------------------ FUNCTION-BASED VIEW ------------------

# This is a function-based view (another way to build pages)
# 'request' contains information about the user visiting the page
def contact_me(request):
    
    # This line is commented out (won’t run)
    # It would just display plain text instead of an HTML page
    # return HttpResponse("Hello World from a Function Base View")
    
    # This renders (loads) the contact.html page
    # 'request' is required so Django knows who is making the request
    return render(request, "pages/contact.html")