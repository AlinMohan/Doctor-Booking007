from django.contrib import admin
from app1.models import User,Doctor,Booking,Complaint

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','Firstname','Lastname','Place','Phone','Email','Department','Username','Password')


admin.site.register(Doctor,DoctorAdmin)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','DoctorName','Department','Date_Time','PatientName')

admin.site.register(Booking,BookingAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','Firstname','Lastname','Place','Phone','Email','Username','Password')

admin.site.register(User,UserAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id','ComplaintType','Date','PatientName','PhoneNumber','Place')

admin.site.register(Complaint,ComplaintAdmin)
