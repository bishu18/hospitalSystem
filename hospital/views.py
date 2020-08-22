from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.db.models import Count
# import json
# from rest_framework import viewsets
# from .serializers import PatientSerializer
# Create your views here.
def about(request):
    return render(request, 'about.html')

def chart(request):
    return render(request, 'chart.html')


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

# LOGIN PAGE.................................................................................................

def login_staff(request):
    error= ""
    if request.method =='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_authenticated:
                login(request, user)
                error= "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login_staff.html', d)

def login_admin(request):
    error= ""
    if request.method =='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_superuser:
                login(request, user)
                error= "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login_admin.html', d)

def login_doctor(request):
    error= ""
    if request.method =='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_authenticated:
                login(request, user)
                error= "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login_doctor.html', d)


# HOME PAGE....................................................................................................

def staff_home(request):
    if not request.user.is_staff:
        return redirect('login_staff')
    return render(request, 'staff_home.html')

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    return render(request, 'admin_home.html')



# VIEW PAGE.....................................................................................................

def doctor_view(request):
    if not request.user.is_superuser:
        return redirect('login_admin')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'doctor_view.html', d)

def branch_view(request):
    if not request.user.is_superuser:
        return redirect('login_admin')
    branch = Branch.objects.all()
    b = {'branch':branch}
    return render(request, 'branch_view.html', b)

def staff_view(request):
    if not request.user.is_superuser:
        return redirect('login_admin')
    staff = Staff.objects.all()
    s = {'staff':staff}
    return render(request, 'staff_view.html', s)

def patient_view(request):
    if not request.user.is_staff:
        return redirect('login_staff')
    patient = Patient.objects.all()
    p = {'patient':patient}
    return render(request, 'patient_view.html', p)

# ADD PAGE....................................................................................................

def doctor_add(request):
    error= ""
    if not request.user.is_superuser:
        return redirect('login_admin')
    if request.method =='POST':
        ud = request.POST['uname']
        pd = request.POST['pwd']
        e = request.POST['mail']
        n = request.POST['name']
        m = request.POST['mobile']
        s = request.POST['special']
        # user = authenticate(username=u, password=p)
        try:
            user = User.objects.create_user(username=ud, password=pd, is_staff=True)
            Doctor.objects.create(user=user ,mail=e, name=n, mobile=m, special=s)
            error= "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'doctor_add.html', d)


def branch_add(request):
    error= ""
    if not request.user.is_superuser:
        return redirect('login_admin')
    if request.method =='POST':
        n = request.POST['name']
        r = request.POST['rate']
        # user = authenticate(username=u, password=p)
        try:
            Branch.objects.create(name=n, rate=r)
            error= "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'branch_add.html', d)

def staff_add(request):
    error= ""
    if not request.user.is_superuser:
        return redirect('login_admin')
    if request.method =='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        e = request.POST['mail']
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        # user = authenticate(username=u, password=p)
        try:
            user = User.objects.create_user(username=u, password=p, is_staff=True)
            Staff.objects.create(user=user, mail=e, name=n, gender=g, mobile=m, address=a)
            error= "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'staff_add.html', d)

def patient_add(request):
    error= ""
    if not request.user.is_staff:
        return redirect('login_staff')
    if request.method =='POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        d = request.POST['age']
        a = request.POST['address']
        r = request.POST['registered']
        # user = authenticate(username=u, password=p)
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, age=d, address=a, registered=r)
            error= "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'patient_add.html', d)

# DELETE PAGE...............................................................................................

def doctor_delete(request, did):
    if not request.user.is_superuser:
        return redirect('login_admin')
    doctor = Doctor.objects.get(id=did)
    doctor.delete()
    return redirect('doctor_view')

def branch_delete(request, bid):
    if not request.user.is_superuser:
        return redirect('login_admin')
    branch = Branch.objects.get(id=bid)
    branch.delete()
    return redirect('branch_view')

def staff_delete(request, sid):
    if not request.user.is_superuser:
        return redirect('login_admin')
    staff = Staff.objects.get(id=sid)
    staff.delete()
    return redirect('staff_view')

def patient_delete(request, pid):
    if not request.user.is_staff:
        return redirect('login_staff')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('patient_view')

# LOGOUT PAGE...............................

def Logout_admin(request):
    logout(request)
    return redirect('login_admin')

def Logout_doctor(request):
    logout(request)
    return redirect('login_doctor')

def Logout_staff(request):
    logout(request)
    return redirect('login_staff')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user = user)
    d = {'data':data, 'user':user}
    return render(request, 'profile.html')

def patient_list(request):
    if not request.user.is_staff:
        return redirect('login_doctor')
    reg = Patient.objects.all().values('registered').annotate(total=Count('id'))
    p = {'reg':reg}
    return render(request, 'patient_list.html', p)

def patient_graph(request):
    if not request.user.is_staff:
        return redirect('login_doctor')
    # regs = Patient.objects.all().values('registered').annotate(total=Count('id'))
    # g = {'regs': reg}
    return render(request, 'patient_graph.html')

# # array = ([
# #       ['Year', 'Sales', 'Expenses'],
# #       ['2004',  1000,      400],
# #       ['2005',  1170,      460],
# #       ['2006',  660,       1120],
# #       ['2007',  1030,      540]
# #     ]);
# # args['array']= array
# # return render_to_response('progress.html',args)

# # context= {'array': json.dumps(array)}
# # return render(request,'progress.html',context)
# # return render_to_response('progress.html',{'array': json.dumps(array)})


# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all().values('registered').annotate(total=Count('id'))
#     serializer_class = PatientSerializer