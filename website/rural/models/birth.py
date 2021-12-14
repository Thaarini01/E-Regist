from django.db import models






class Birth(models.Model):
    FirstName=models.CharField(max_length=50)
    MiddleName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    DateOfBirth=models.DateField(max_length=50)
    PlaceOfBirth=models.CharField(max_length=50) 
    TimeOfBirth=models.TimeField(max_length=50)
    Name_Of_Father=models.CharField(max_length=50) 
    Name_Of_Mother=models.CharField(max_length=50)
    DateOfRegistration=models.DateField(max_length=50)
    Registration_Number=models.CharField(max_length=40)
    