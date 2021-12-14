from django.db import models









class Register(models.Model):
    FirstName=models.CharField(max_length=50)
    MiddleName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    DateOfBirth=models.DateField(max_length=50)
    Gender=models.CharField(max_length=50)
    Address=models.TextField(max_length=100)
    MobileNumber=models.CharField(max_length=10)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    Re_Enter_Password=models.CharField(max_length=50)
    