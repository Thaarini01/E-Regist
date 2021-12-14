from django.db import models







class Death(models.Model):
    FirstName=models.CharField(max_length=50)
    MiddleName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    DateOfBirth=models.DateField(max_length=50)
    Age=models.CharField(max_length=3)
    Blood_Group=models.CharField(max_length=30)
    Religion=models.CharField(max_length=30)
    Caste=models.CharField(max_length=30)
    Community=models.CharField(max_length=30)
    Name_Of_Father=models.CharField(max_length=50) 
    Name_Of_Mother=models.CharField(max_length=50)
    Name_Of_Spouse=models.CharField(max_length=50) 
    Occupation=models.CharField(max_length=50) 
    Address=models.TextField(max_length=100)
    Pincode=models.CharField(max_length=6)
    MobileNumber=models.CharField(max_length=10)
    Email=models.EmailField(max_length=50)
    PlaceOfDeath=models.CharField(max_length=50) 
    DateOfDeath=models.DateField(max_length=30)
    TimeOfDeath=models.TimeField(max_length=50)
    HospitalName=models.CharField(max_length=30)
    DeathAddress=models.TextField(max_length=50)
    # Pincode_Of_Death_Address=models.IntegerField(max_length=6)
    Problems_Of_Deceased=models.TextField(max_length=100)
    Actual_Reason=models.TextField(max_length=100)
    Cause_Of_Death=models.TextField(max_length=100)
    Female_Death=models.TextField(max_length=100)
    Habitual_Smoker=models.TextField(max_length=100) 
    Tobacco_User=models.TextField(max_length=100)
    Forms_Of_Tobacco=models.TextField(max_length=100) 
    Alcoholic_Person=models.TextField(max_length=100)
    Remarks=models.TextField(max_length=100)
    
    