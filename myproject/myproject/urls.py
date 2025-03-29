from django.contrib import admin
from django.urls import path
from myapp.views import directory_view, login_view, logout_view, billing_view, account_view, scheduler_view  # Import the login view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directory/', directory_view, name='directory'),
    path('login/', login_view, name='login'),  # Add the login URL
    path('logout/', logout_view, name='logout'),
    path('billing/', billing_view, name='billing'),
    path('account/', account_view, name='account'),
    path('scheduler/', scheduler_view, name='scheduler'),
]