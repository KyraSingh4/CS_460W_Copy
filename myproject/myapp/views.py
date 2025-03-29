from django.shortcuts import render, redirect
from Directory import Directory  # Use relative import
from Authenticator import Authenticator  # Import the Authenticator class
from Member import Member, President, BillingStaff
from Calendar import Calendar
import datetime

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
        elif request.POST.get('submittype') == 'Update Member':
            mem = President()
            mem.updateInformation(request.POST.get('member_id'), request.POST.get('attribute'), request.POST.get('value'))
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
        if request.POST.get('submittype') == 'Modify Charge':
            mem = BillingStaff()
            mem.modifyBill(request.POST.get('charge_id'), request.POST.get('attribute'), request.POST.get('value'))
            success = True
            return render(request, 'myapp/billing.html', {'success': success})
        if request.POST.get('submittype') == 'Delete Charge':
            mem = BillingStaff()
            mem.deleteCharge(request.POST.get('charge_id'))
            success = True
            return render(request, 'myapp/billing.html', {'success': success})

    return render(request, 'myapp/billing.html')

def scheduler_view(request):
    results = None
    cal = Calendar()
    dir = Directory()
    if request.method == 'POST':
        if request.POST.get('submittype') == 'Reset Process':
            request.session['day'] = None
            request.session['scheduler_stage'] = None
            request.session['num_guests'] = None
        elif request.POST.get('submittype') == 'Select Day':
            request.session['day'] = request.POST.get('day')
            request.session['scheduler_stage'] = 'Type' # Move to the next stage
            results = cal.RetrieveDay(request.POST.get('day'))
            return render(request, 'myapp/scheduler.html', {'results': results})
        elif request.POST.get('submittype') == 'Select Type':
            request.session['type'] = request.POST.get('type')
            request.session['scheduler_stage'] = 'Guests' # Move to the next stage
            results = cal.RetrieveDay(request.session['day'])
            return render(request, 'myapp/scheduler.html', {'results': results})
        elif request.POST.get('submittype') == 'Designate Guests':
            request.session['num_guests'] = request.POST.get('guests')
            request.session['scheduler_stage'] = 'Reserve' # Move to the next stage
            results = cal.RetrieveDay(request.session['day'])
            return render(request, 'myapp/scheduler.html', {'results': results})
        elif request.POST.get('submittype') == 'Reserve':
            start = request.POST.get('start')
            start = start.split(":")
            end = request.POST.get('end')
            end = end.split(":")
            court = request.POST.get('court')
            if request.session.get('type') == 'singles':
                mem = Member(request.session.get('member_id'))
                if request.session.get('num_guests') == '1': # 1 guest pass, 1 member
                    members = []
                    guests = [request.POST.get('guest1')]
                else: # 0 guest passes, 2 members
                    mem2 = request.POST.get('member2')
                    mem2 = mem2.split(" ")
                    members = [dir.nameLookup(mem2[0], mem2[1])]
                    guests = []
                mem.createReservation(request.session.get('type'), request.session.get('day'), 
                                      datetime.time(int(start[0]),int(start[1])), datetime.time(int(end[0]),int(end[1])), court, members, guests)
            elif request.session.get('type') == 'doubles':
                mem = Member(request.session.get('member_id'))
                match request.session.get('num_guests'):
                    case '1':  # 1 guest pass, 3 members
                        mem2 = request.post.get('member2')
                        mem2 = mem2.split(" ")
                        mem3 = request.post.get('member3')
                        mem3 = mem3.split(" ")
                        members = [dir.nameLookup(mem2[0],mem2[1]), dir.nameLookup(mem3[0],mem3[1])]
                        guests = [request.POST.get('guest1')]
                    case '2':  # 2 guest passes, 2 members
                        mem2 = request.post.get('member2')
                        mem2 = mem2.split(" ")
                        members = [dir.nameLookup(mem2[0],mem2[1])]
                        guests = [request.POST.get('guest1'), request.POST.get('guest2')]
                    case '3':  # 3 guest passes, 1 member
                        members = []
                        guests = [request.POST.get('guest1'), request.POST.get('guest2'), request.POST.get('guest3')]
                    case '0':  # 0 guest passes, 4 members
                        mem2 = request.post.get('member2')
                        mem2 = mem2.split(" ")
                        mem3 = request.post.get('member3')
                        mem3 = mem3.split(" ")
                        mem4 = request.POST.get('member4')
                        mem4 = mem4.split(" ")
                        members = [dir.nameLookup(mem2[0],mem2[1]), dir.nameLookup(mem3[0],mem3[1]), dir.nameLookup(mem4[0],mem4[1])]
                        guests = []
                mem.createReservation(request.session.get('type'), request.session.get('day'), 
                                      datetime.time(int(start[0]),int(start[1])), datetime.time(int(end[0]),int(end[1])), court, members, guests)
            request.session['scheduler_stage'] = None # Reset stage
            return render(request, 'myapp/scheduler.html', {'success': True})
        elif request.POST.get('submittype') == 'Lookup Reservation':
            res_results = cal.lookupReservation(request.POST.get('res_id'))
            attendees = cal.getAttendees(request.POST.get('res_id'))
            return render(request, 'myapp/scheduler.html', {'res_results': res_results, 'attendees' : attendees})
        elif request.POST.get('submittype') == 'Delete Reservation':
            mem = Member(request.session.get('member_id'))
            mem.deleteReservation(int(request.POST.get('res_id')))
            return render(request, 'myapp/scheduler.html', {'success': True})

    return render(request, 'myapp/scheduler.html')

def account_view(request):
    result = None
    if request.method == 'POST':
        if request.POST.get('submittype') == 'Fetch Information':
            mem = Member(request.session.get('member_id'))
            result = mem.getInformation()
            return render(request, 'myapp/account.html', {'result': result})
        if request.POST.get('submittype') == 'Change First Name':
            mem = Member(request.session.get('member_id'))
            mem.updateInformation('firstname', request.POST.get('value'))
            result = mem.getInformation()
            return render(request, 'myapp/account.html', {'result': result})
        if request.POST.get('submittype') == 'Change Last Name':
            mem = Member(request.session.get('member_id'))
            mem.updateInformation('lastname', request.POST.get('value'))
            result = mem.getInformation()
            return render(request, 'myapp/account.html', {'result': result})
        if request.POST.get('submittype') == 'Change Email':
            mem = Member(request.session.get('member_id'))
            mem.updateInformation('email', request.POST.get('value'))
            result = mem.getInformation()
            return render(request, 'myapp/account.html', {'result': result})
        if request.POST.get('submittype') == 'Change Phone Number':
            mem = Member(request.session.get('member_id'))
            mem.updateInformation('phonenum', request.POST.get('value'))
            result = mem.getInformation()
            return render(request, 'myapp/account.html', {'result': result})
        if request.POST.get('submittype') == 'Change Opt-In':
            mem = Member(request.session.get('member_id'))
            mem.updateInformation('optin', request.POST.get('optin'))
            result = mem.getInformation()
            return render(request, 'myapp/account.html', {'result': result})
        if request.POST.get('submittype') == 'Pay Bill':
            mem = Member(request.session.get('member_id'))
            mem.payBill()
            return render(request, 'myapp/account.html', {'result': result})





    return render(request, 'myapp/account.html')