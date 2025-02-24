from django.urls import path
from .views import home  # Import the view

urlpatterns = [
    path('', home, name='home'),  # Home page route
]
