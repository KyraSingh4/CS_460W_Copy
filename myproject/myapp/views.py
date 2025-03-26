from django.shortcuts import render, redirect
from Directory import Directory  # Use relative import
from Authenticator import Authenticator  # Import the Authenticator class

def search_directory(request):
    results = None
    if request.method == 'POST':
        attribute = request.POST.get('attribute')
        value = request.POST.get('value')
        directory = Directory()
        results = directory.searchAttr(request.session.get('member_id'), attribute, value)

    return render(request, 'myapp/search_form.html', {'results': results})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = Authenticator()
        id = auth.login(username, password)
        if id != False:
            request.session['member_id'] = id
            return redirect('search_directory')  # Redirect to the search page on successful login
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid credentials'})

    return render(request, 'myapp/login.html')