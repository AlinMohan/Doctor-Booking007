from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import User
from app1.models import Doctor
from app1.models import Booking
from app1.models import Complaint
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    return render(request,'doctors.html')

def department(request):
    return render(request,'department.html')

def contact(request):
    return render(request,'contact.html')

def signup(request):
    return render(request,'signup.html')
def register(request):
    a = request.POST['fname']
    b = request.POST['lname']
    c = request.POST['place']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['uname']
    g = request.POST['pass']
    h = User(Firstname=a,Lastname=b,Place=c,Phone=d,Email=e,Username=f,Password=g)
    h.save()
    return HttpResponse('User Registered Successfully')

def login(request):
    return render(request,'login.html')

# def login_press(request):
#     try:
#         a = User.objects.get(Username=request.POST['username'])
#         if a.Password == request.POST['password']:
#             request.session['first'] = a.Username
#             return render(request, 'after_loginuser.html',{})
#         else:
#             return HttpResponse('Invalid password')
#     except:
#         return HttpResponse('User does not exist')

# def after_loginuser(request):
#     return render(request,'after_loginuser.html')

def loged(request):
    try:
        a = User.objects.get(Username=request.POST['username'])
        if a.Password==request.POST['password']:
            request.session['first']= a.Username
            return render(request,'signin.html',{'key':a.Username,'key2':a.Firstname,'key3':a.Lastname,'key4':a.Place,'key5':a.Phone,'key6':
                                                 a.Email})
        else:
            return HttpResponse('Invalid password')
    except:
        return HttpResponse('User does not exist')

def userlogout(request):
    del request.session['first']
    # return home(request)
    return redirect('home')

def docreg(request):
    a = request.POST['fname']
    b = request.POST['lname']
    c = request.POST['place']
    d = request.POST['phone']
    e = request.POST['email']
    i = request.POST['dept']
    f = request.POST['uname']
    g = request.POST['pass']
    h = Doctor(Firstname=a,Lastname=b,Place=c,Phone=d,Email=e,Department=i,Username=f,Password=g)
    h.save()
    return HttpResponse('Successfully Registered')

def doclogin(request):
    return render(request,'doctorlogin.html')


def doclog(request):
    try:
        a = Doctor.objects.get(Username=request.POST['username'])
        if a.Password==request.POST['password']:
            request.session['first']= a.Username
            return render(request,'docsignin.html',{'key':a.Username,'key2':a.Firstname,'key3':a.Lastname,'key4':a.Place,'key5':a.Phone,'key6':
                                                 a.Email,'key7':a.Department})
        else:
            return HttpResponse('Invalid password')
    except:
        return HttpResponse('Doctor does not exist')

def doclogout(request):
    del request.session['first']
    return home(request)

def booking(request):
    a = Doctor.objects.all()
    return render(request,'booking.html',{'key1':a})

def booked(request):
    a = request.POST['docname']
    b = request.POST['dept']
    c = request.POST['date1']
    d = request.POST['patname']
    h = Booking(DoctorName=a,Department=b,Date_Time=c,PatientName=d)
    h.save()
    return HttpResponse('Appointment Registered Successfully')

def complaint(request):
    return render(request,'complaint.html')

def complainting(request):
    a = request.POST['comp']
    b = request.POST['date']
    c = request.POST['patname']
    d = request.POST['phone']
    e = request.POST['place']
    h = Complaint(ComplaintType=a,Date=b,PatientName=c,PhoneNumber=d,Place=e)
    h.save()
    return HttpResponse('Complaint Registered Successfully')



