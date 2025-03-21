from django.contrib import admin
from django.urls import path
from myapp.views import search_directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_directory, name='search_directory'),
]