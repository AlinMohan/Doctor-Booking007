from django.db import models

# Create your models here.
class User(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Place = models.TextField()
    Phone = models.IntegerField()
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Firstname



class Doctor(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Place = models.TextField()
    Phone = models.IntegerField()
    Email = models.EmailField()
    Department = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Firstname

class Booking(models.Model):
    DoctorName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Date_Time = models.DateTimeField()
    PatientName = models.CharField(max_length=100)

    def __str__(self):
        return self.DoctorName

class Complaint(models.Model):
    ComplaintType = models.TextField()
    Date = models.DateField()
    PatientName = models.CharField(max_length=100)
    PhoneNumber = models.IntegerField(null=True)
    Place = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.PatientName




