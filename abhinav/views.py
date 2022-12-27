
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login
from django.contrib import messages
from website import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,"abhinav/index.html")


def signup(request):
    if request. method == "POST":
        username = request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if User.objects.filter(username=username):
            messages.error(request,"username already exist!")
        if User.objects.filter(email=email):
            messages.error(request,"'Email already exixts!")
            

        if len(username)>15:
            messages.error(request,"Username must be less than 15 characters!")
        if pass1 != pass2:
            messages.error(request,"Passwords Do not match!")
        if not username.isalnum():
            messages.error(request,"username name must be aplha numeric.")        


        myuser=User.objects.create_user (username,email,pass1)
        myuser.first_name= fname
        myuser.last_name= lname

        myuser.save()

        messages.success(request,"your accoount has successfully been created")

        # welcome email

        subject= "welcome to Abhinav pvt lmt"
        message= "Hello"+ myuser.first_name + "!! \n" "Welcome to Abhinav private limited \n We are very glad that you visited our webiste \n We have sent you a confirmation email ,Please confirm your email address to activate your acount. /n Thanks a lot,Abhinav Dubey"
        from_email= settings.EMAIL_HOST_USER
        to_list =[ myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)        

       

        return redirect('signin')







    return render(request,"abhinav/signup.html")

def signin(request):
    if request.method =="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        
        
        user= auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')
        else:
            return redirect('signin')
    return render(request,"abhinav/signin.html")
def mainpage(request):
    
    return render(request,"abhinav/mainpage.html")

    
    

