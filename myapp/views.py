from django.shortcuts import redirect, render
from .forms import SignupForm, NotesForm, FeedbackForm
from .models import user_signup
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings
import requests
import json
import random

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get("signup")=="signup": #child
            newuser=SignupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created successfully!")

                #Email Send Code
                sub="Welcome!"
                msg=f"Dear User,\n\nYour account has been created with us!\n Enjoy our services. \nIf any query, Contact us,\n+91 9724799469 | sanket.tops@gmail.com"
                from_ID=settings.EMAIL_HOST_USER
                #to_ID=["yashhirapara.b@gmail.com","kanjiyaharshit@gmail.com","jadejamayurdhvajsinh9898556@gmail.com","jinalfadadu94@gmail.com"]
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                return redirect("notes")
            else:
                print(newuser.errors)
        elif request.POST.get("login")=="login": #child
            if request.POST["username"]=="" and request.POST["password"]=="":
                return redirect("custom_error")
            else:
                unm=request.POST["username"]
                pas=request.POST["password"]

                user=user_signup.objects.filter(username=unm,password=pas)
                userid=user_signup.objects.get(username=unm)
                print("UserID:",userid.id)    

                if user: #true
                    print("Login successfully!")
                    request.session["user"]=unm
                    request.session["userid"]=userid.id

                    # SMS Send Code
                    # mention url
                    otp=random.randint(1111,9999)
                    url = "https://www.fast2sms.com/dev/bulk"
                    my_data = {
                        # Your default Sender ID
                        'sender_id': 'FSTSMS',
                        
                        # Put your message here!
                        'message': f'Hello, Your account has been logdin! Your OTP is {otp}',
                        
                        'language': 'english',
                        'route': 'p',
                        
                        # You can send sms to multiple numbers
                        # separated by comma.
                        'numbers': '9316312117, 7016688740, 7383872727, 9426913979'	
                    }

                    # create a dictionary
                    headers = {
                        'authorization': 'eNB2jE9KVhwkSpvnfTIxudmyoHPXrJWQ3z76aFl8iAsCtR5OMb2EXaQmJ8tzi0brTIONRgHK5jZ9cMVs',
                        'Content-Type': "application/x-www-form-urlencoded",
                        'Cache-Control': "no-cache"
                    }
                    # make a post request
                    """response = requests.request("POST",
                                                url,
                                                data = my_data,
                                                headers = headers)"""
                    #load json data from source
                    #returned_msg = json.loads(response.text)
                    #returned_msg = json.loads("MSG Send Successfully!")
                    # print the send message
                    #print(returned_msg['message'])
                    return redirect("notes")
                else:
                    print("Error...Login fail!")
                    return redirect('custom_Error')
    return render(request,'index.html')

def notes(request):
    user=request.session.get("user")
    if request.method=="POST":
        Myfrm=NotesForm(request.POST,request.FILES)
        if Myfrm.is_valid():
            Myfrm.save()
            print("Your post has been uploaded!")
        else:
            print(Myfrm.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        newfeedback=FeedbackForm(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your Feedback has been saved!")
        else:
            print(newfeedback.errors)
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect("/")

def updateprofile(request):
    user=request.session.get("user")
    userid=request.session.get("userid")
    uid=user_signup.objects.get(id=userid)
    if request.method=="POST":
        updateUser=SignupForm(request.POST)
        if updateUser.is_valid():
            updateUser=SignupForm(request.POST,instance=uid)
            updateUser.save()
            print("Your Profile has been updated!")
            return redirect("notes")
        else:
            print(updateUser.errors)
    return render(request,'updateprofile.html',{'user':user,"cuser":user_signup.objects.get(id=userid)})

def custom_error(request):
    return render(request,'custom_error.html')