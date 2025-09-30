from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name_data=request.POST['firstname']
        last_name_data=request.POST['lastname']
        email_data=request.POST['email']
        username_data=request.POST['username']
        password_data=request.POST['password']
        print(first_name_data,last_name_data,email_data,username_data,password_data)
        u= User.objects.create(
            first_name=first_name_data,
            last_name=last_name_data,
            email=email_data,
            username=username_data
        )
        u.set_password(password_data)
        u.save()
        return redirect('login_')
    return render(request,'register.html')

def login_(request):
    if request.method == 'POST':
        username_data=request.POST['username']
        password_data=request.POST['password']
        u=authenticate(username=username_data,password=password_data)
        print(u) 
        if u:
            login(request,u)
            return redirect('home')       
    return render(request,'login_.html')

def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    
def change_password(request):
    if request.method == 'POST':
        try:
            u=User.objects.get(username=request.user.username)
            old_pass_data=request.POST['oldpassword']
            old_pass_verified=authenticate(username=u.username,password=old_pass_data)
            if old_pass_verified:
                print('Old password is matching')
                return render(request,'change_password.html',{'oldpassword_match':True})
            else:
                return render(request,'change_password.html',{'oldpassword_notmatch':True})
        except:
                new_pass_data=request.POST['newpassword']
                u.set_password(new_pass_data)
                u.save()
                return redirect('login_')
    return render(request,'change_password.html')

def update_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.save()
        messages.success(request, "Profile updated successfully!")

        return redirect("profile")

    return render(request, "update_profile.html") 
