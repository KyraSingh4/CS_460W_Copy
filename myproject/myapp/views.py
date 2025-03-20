from django.shortcuts import render
from .Directory import Directory  # Use relative import

def search_directory(request):
    results = None
    if request.method == 'POST':
        attribute = request.POST.get('attribute')
        value = request.POST.get('value')
        directory = Directory()
        results = directory.searchAttr(1, attribute, value)  # Assuming memberid 1 for admin view

    return render(request, 'myapp/search_form.html', {'results': results})