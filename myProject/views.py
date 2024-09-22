from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from myApp.models import *
from django.contrib import messages

from django.utils import timezone
from pytz import timezone as pytz_timezone


@login_required
def homePage(req):
    
    user = req.user
    
    context = {
        'user':user
    }
    
    return render(req,'myAdmin/index.html',context)

def registerPage(req):
    
    if req.method == 'POST':
        
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirmPassword')
        
        if password == confirm_password:
            user = Custom_User.objects.create_user(
                username = req.POST.get('username'),
                first_name= req.POST.get('firstname'),
                last_name= req.POST.get('lastname'),
                user_type = req.POST.get('userType'),
                email = req.POST.get('email'),
                password = confirm_password
            )
            user.save()
            messages.success(req, "Registration successful! You can now log in.")
            return redirect('loginPage')
        else:
            messages.error(req, 'Passwords do not match. Please try again.')
    
    return render(req, 'common/register.html')


def loginPage(req):
    
    if req.method == 'POST':
        
        user_name = req.POST.get('username')
        password = req.POST.get('password')
        
        
        user = authenticate(req,username = user_name,password = password)
        
        if user:
            login(req,user)
            return redirect('homePage')
        
        else:
            messages.error(req, "Invalid username or password.")
        
    return render(req, 'common/login.html')


def logoutPage(req):
    
    logout(req)
    
    return redirect('loginPage')


@login_required
def adminProfile(req):
    
    user = req.user

    if user.user_type == "admin":

        last_login = user.last_login
        
        if last_login:
            # Convert last_login to a specific timezone (e.g., 'Asia/Dhaka')
            user_last_login = last_login.astimezone(pytz_timezone('Asia/Dhaka'))

        return render(req, 'myAdmin/profile.html', {'last_login':user_last_login})
    
    else:
       return render(req, 'myAdmin/error.html')



@login_required
def createResume(req):

    user = req.user
    current_user = user
    if user.user_type == 'user':

        if req.method == 'POST':
            

            # resume = Resume_Model(
            #     user = current_user,
            #     profile_pic = req.FILES.get('profile_pic'),
            #     designation = req.POST.get('designation'),
            #     career_summary = req.POST.get('career_summary'),
            #     address = req.POST.get('address'),
            #     contact_no = req.POST.get('contact_no'),
            #     linkedin_url = req.POST.get('linkedin_url'),
            #     gender = req.POST.get('gender')
            # )

            # another way

            resume, created = Resume_Model.objects.get_or_create(user=current_user)
                
            resume.profile_pic = req.FILES.get('profile_pic')
            resume.designation = req.POST.get('designation')
            resume.career_summary = req.POST.get('career_summary')
            resume.address = req.POST.get('address')
            resume.contact_no = req.POST.get('contact_no')
            resume.linkedin_url = req.POST.get('linkedin_url')
            resume.gender = req.POST.get('gender')
            

            resume.save()

            current_user.first_name = req.POST.get('firstName')
            current_user.last_name = req.POST.get('lastName')

            current_user.save() 
            messages.success(req, 'Resume successfully created!')
            return redirect('viewResume')
        return render(req, 'myAdmin/createResume.html')

    else:
        return render(req, 'myAdmin/error.html')



@login_required    
def addEducationPage(req):

    user = req.user

    if user.user_type == "admin":

        return render(req,'myAdmin/addEducation.html')
    
    else:
        return render(req, 'myAdmin/error.html')


@login_required    
def addSkillPage(req):

    user = req.user

    if user.user_type == "admin":

        return render(req,'myAdmin/addSkill.html')
    
    else:
        return render(req, 'myAdmin/error.html')


@login_required
def addLanguagePage(req):

    user = req.user

    if user.user_type =='admin':

        return render(req,'myAdmin/addLanguage.html')
    else:
        return render(req,'myAdmin/error.html')
    
def addInterestPage(req):
    
    user = req.user

    if user.user_type == 'admin':
        return render(req, 'myAdmin/addInterest.html')
    else:
        return render(req,'myAdmin/error.html')


@login_required
def viewResume(req):

    user = req.user

    if user.user_type == 'user':
        current_user = user
        resume = get_object_or_404(Resume_Model, user=current_user)
        context = {
            'resume':resume,
        }
        return render(req, 'myAdmin/user-profile.html', context)
    
    else:
        return render(req,'myAdmin/error.html')