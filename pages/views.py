from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

# Class based views
class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
class AboutPageView(TemplateView):
    template_name = "pages/about.html"

# function based views
def contact_me(request):
    # return HttpResponse("Hello World from a Function Base View")
    return render(request, "pages/contact.html")