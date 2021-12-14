from django.db import models









class Login(models.Model):
    FirstName=models.CharField(max_length=50)
    MiddleName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    