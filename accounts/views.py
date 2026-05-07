from django.shortcuts import render # to render the template
from django.contrib.auth.forms import UserCreationForm # to create a user registration form
from django.urls import reverse_lazy # to redirect to a page after successful registration
from django.views.generic import CreateView # to create a view for user registration

# Create your views here.

class SignUpView(CreateView): # CreateView is a generic view that allows us to create a new object, in this case, a new user
    template_name = 'registration/signup.html' # the template that will be used to render the registration form
    
    # form_class attribute allows to create from a form
    # we use this one when we want to have a custom form
    form_class = UserCreationForm # the form that will be used to create a new user, we can also create our own form by inheriting from UserCreationForm and adding more fields
    success_url = reverse_lazy('login') # after successful registration, redirect to login page 
    