from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from . models.birth import Birth
from .models import *
from . models.death import Death
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
           
			login(request,user)
			messages.success(request, "Registration successful." )
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def loginpage(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
        
   
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('/home')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

# def logout_user(request):
# 	logout(request)
# 	# messages.info(request, "You have successfully logged out.") 
# 	return HttpResponse("Logged Out")
# # Create your views here.

# def logout_user(request):
#     if request.method=="POST":
#         logout(request)
#         return redirect (request,"loginpage")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('login')
        

def home(request):
    return render (request, 'home.html')


@login_required
def birth(request):
    if(request.method == "GET"): 
        return render(request, 'birth.html') 
    else:
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        birthplace=request.POST.get('birthplace')
        birthtime=request.POST.get('birthtime')
        father=request.POST.get('father')
        mother=request.POST.get('mother')
        registration=request.POST.get('registration')
        number=request.POST.get('number')
        
        birth = Birth(FirstName=fname,MiddleName=mname,LastName=lname,Gender=gender,DateOfBirth=dob,PlaceOfBirth=birthplace,TimeOfBirth=birthtime,Name_Of_Father=father, Name_Of_Mother=mother,DateOfRegistration=registration,Registration_Number=number)
        birth.save()
        # return HttpResponse(f'{fname} {mname} {lname} {gender} {dob} {birthplace} {birthtime} {father} {mother} {registration} {number}')

        return render(request,'birthresponse.html')
        
       
def death(request):
    if(request.method == "GET"):
        return render(request, 'death.html')
    else:
        firstname=request.POST.get('firstname')
        middlename=request.POST.get('middlename')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        dateofbirth=request.POST.get('dateofbirth') 
        age=request.POST.get('age')
        bloodgroup=request.POST.get('bloodgroup')
        religion=request.POST.get('religion')
        caste=request.POST.get('caste')
        community=request.POST.get('community')
        fathername=request.POST.get('fathername')
        mothername=request.POST.get('mothername')
        spouse=request.POST.get('spouse')
        occupation=request.POST.get('occupation')
        add=request.POST.get('add')
        code=request.POST.get('code')
        phone=request.POST.get('phone')
        mail=request.POST.get('mail')
        deathplace=request.POST.get('deathplace')
        deathdate=request.POST.get('deathdate')
        deathtime=request.POST.get('deathtime')
        hospital=request.POST.get('hospital')
        deathadd=request.POST.get('deathadd')
        # pin=request.POST.get('pin')
        problem=request.POST.get('problem')
        reason=request.POST.get('reason')
        cause=request.POST.get('cause')
        female=request.POST.get('female')
        smoke=request.POST.get('smoke')
        tobacco=request.POST.get('tobacco')
        forms=request.POST.get('forms')
        alcohol=request.POST.get('alcohol')
        remarks=request.POST.get('remarks')
        
        death = Death(FirstName=firstname,MiddleName=middlename,LastName=lastname,Gender=gender,DateOfBirth=dateofbirth,Age=age,Blood_Group=bloodgroup,Religion=religion,Caste=caste,Community=community,Name_Of_Father=fathername,Name_Of_Mother=mothername,Name_Of_Spouse=spouse,Occupation=occupation,Address=add,Pincode=code,MobileNumber=phone,Email=mail,PlaceOfDeath=deathplace,DateOfDeath=deathdate,TimeOfDeath=deathtime,HospitalName=hospital,DeathAddress=deathadd,Problems_Of_Deceased=problem,Actual_Reason=reason,Cause_Of_Death=cause,Female_Death=female,Habitual_Smoker=smoke,Tobacco_User=tobacco,Forms_Of_Tobacco=forms,Alcoholic_Person=alcohol,Remarks=remarks)
        death.save()
        # return HttpResponse(f'{firstname} {middlename} {lastname} {gender} {dateofbirth} {age} {bloodgroup} {religion} {caste} {community} {fathername} {mothername} {spouse} {occupation} {add} {code} {phone} {mail} {deathplace}')
    
        return render(request,'deathresponse.html')