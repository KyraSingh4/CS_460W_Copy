from django.contrib import admin
from django.urls import path
from myapp.views import search_directory, login_view  # Import the login view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_directory, name='search_directory'),
    path('login/', login_view, name='login'),  # Add the login URL
]