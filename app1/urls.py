from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('doctors',views.doctors,name='doctors'),
    path('department',views.department,name='department'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('loging',views.register,name='register'),
    path('login',views.login,name='login'),
    # path('login_press',views.login_press,name='login_press'),
    path('loged',views.loged,name='loged'),
    path('home',views.userlogout,name='userlogout'),
    path('docreg',views.docreg,name='docreg'),
    path('doclogin',views.doclogin,name='doclogin'),
    path('doclog',views.doclog,name='doclog'),
    path('home',views.doclogout,name='doclogout'),
    path('booking',views.booking,name='booking'),
    path('booked',views.booked,name='booked'),
    path('complaint',views.complaint,name='complaint'),
    path('complainting',views.complainting,name='complainting'),

]