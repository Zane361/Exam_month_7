from django.shortcuts import render, redirect
from main import models
from main.functions import staff_required
from django.contrib.auth import authenticate, login, logout


@staff_required
def index(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

# ----- AUTHETICATION -----

def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                return redirect('dashboard:index')
            else:
                return render(request, 'dashboard/auth/login.html')
        except:
            return redirect('dashboard:login')
    return render(request, 'dashboard/auth/login.html')

def log_out(request):
    logout(request)
    return redirect('dashboard:login')

# ----- PROFILE -----

@staff_required
def profile_edit(request):
    if request.method == 'POST':
        username = request.user.username
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        new_password_confirm = request.POST.get('new_password_confirm')
        if authenticate(username=username, password=password):
            user = models.User.objects.get(username=username)
            user.first_name = first_name if first_name else ''
            user.last_name = last_name if last_name else ''
            if new_password and new_password == new_password_confirm:
                user.set_password(new_password)
            user.save()
            return redirect('dashboard:index')
    context = {
        'user':request.user
    }
    return render(request, 'dashboard/auth/edit.html', context)

# ----- STAFF -----

@staff_required
def staff_create(request):
    if request.method == 'POST':
        models.Staff.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            salary = request.POST['salary']
        )
        return redirect('dashboard:staff_list')
    return render(request, 'dashboard/staff/create.html')

@staff_required
def staff_list(request):
    queryset = models.Staff.objects.all()
    context = {
        'queryset':queryset
    }
    return render(request, 'dashboard/staff/list.html', context)

@staff_required
def staff_detail(request, id):
    staff = models.Staff.objects.get(id=id)
    context = {
        'staff':staff
    }
    return render(request, 'dashboard/staff/detail.html', context)

@staff_required
def staff_update(request, id):
    staff = models.Staff.objects.get(id=id)
    if request.method == 'POST':
        staff.first_name = request.POST['first_name']
        staff.last_name = request.POST['last_name']
        staff.salary = request.POST['salary']
        staff.save()
        return redirect('dashboard:staff_list')
    context = {
        'staff':staff
    }
    return render(request, 'dashboard/staff/update.html', context)

@staff_required
def staff_delete(request, id):
    staff = models.Staff.objects.get(id=id)
    staff.delete()
    return redirect('dashboard:staff_list')

# ----- ATTENDANCE ----- 

@staff_required
def attendance_list(request):
    queryset = models.Attendance.objects.all()
    context = {
        'queryset':queryset
    }
    return render(request, 'dashboard/attendance/list.html', context)
