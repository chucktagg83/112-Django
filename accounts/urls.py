from django.urls import path
from .views import SignUpView

urlpatterns = [ 
    
    # path('login/', views.login_view, name='login')
    path('signup/', SignUpView.as_view(), name='signup'),
]
    