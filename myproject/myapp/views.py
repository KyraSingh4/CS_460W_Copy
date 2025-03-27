from django.shortcuts import render, redirect
from Directory import Directory  # Use relative import
from Authenticator import Authenticator  # Import the Authenticator class
from Member import Member, President, BillingStaff

def directory_view(request):
    results = None
    success = None
    if request.method == 'POST':
        directory = Directory()
        if request.POST.get('submittype') == 'View the Full Directory':
            results = directory.getAll(request.session.get('member_id'))
            return render(request, 'myapp/directory.html', {'results': results})
        elif request.POST.get('submittype') == 'Search':
            attribute = request.POST.get('attribute')
            value = request.POST.get('value')
            results = directory.searchAttr(request.session.get('member_id'), attribute, value)
            return render(request, 'myapp/directory.html', {'results': results})
        elif request.POST.get('submittype') == 'Create Member':
            mem = President()
            mem.createMember(request.POST.get('fname'), request.POST.get('lname'), request.POST.get('email'),
                             request.POST.get('phonenum'), request.POST.get('optin'), request.POST.get('password'))
            success = True
            return render(request, 'myapp/directory.html', {'success': success})
        elif request.POST.get('submittype') == 'Deactivate Member':
            mem = President()
            mem.deactivateMember(request.POST.get('memid'))
            success = True
            return render(request, 'myapp/directory.html', {'success': success})

    return render(request, 'myapp/directory.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = Authenticator()
        id = auth.login(username, password)
        if id != False:
            request.session['member_id'] = id
            return redirect('directory')  # Redirect to the search page on successful login
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid credentials'})

    return render(request, 'myapp/login.html')

def logout_view(request):
    if request.method == 'POST':
        request.session['member_id'] = None
        return redirect('login')

    return render(request, 'myapp/logout.html')

def billing_view(request):
    bill = None
    success = None
    if request.method == 'POST':
        if request.POST.get('submittype') == 'Get Bill':
            if request.session.get('member_id') == 1 or request.session.get('member_id') == 2:
                if request.session.get('member_id') == 1:
                    mem = President()
                else:
                    mem = BillingStaff()
                bill = mem.getBill(request.POST.get('mem_id'))
            else:
                mem = Member(request.session.get('member_id'))
                bill = mem.getBill()
            return render(request, 'myapp/billing.html', {'bill': bill})
        if request.POST.get('submittype') == 'Create Charge':
            if request.session.get('member_id') == 1:
                mem = President()
            else:
                mem = BillingStaff()
            mem.addEventFee(request.POST.get('amount'), request.POST.get('desc'), request.POST.get('mem_id'))
            success = True
            return render(request, 'myapp/billing.html', {'success': success})

    return render(request, 'myapp/billing.html')

def account_view(request):
    result = None
    if request.method == 'POST':
        if request.POST.get('submittype') == 'Fetch Information':
            mem = Member(request.session.get('member_id'))
            result = mem.getInformation()
            return render(request, 'myapp/account.html', {'result': result})


    return render(request, 'myapp/account.html')