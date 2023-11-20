from django.shortcuts import render,redirect
from .models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail



def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact=Contact.objects.create(name=name,email=email,number=number,subject=subject,message=message)
        print(contact)
        
        subject = 'Mail From QuickBite'
        message = f'Name={name}\n Email={email}\n Number={number}\n Subject={subject}\n Message={message}'
        from_email = 'iamsatyamnarayan@gmail.com' 
        recipient_list = [from_email]

        send_mail(subject, message, from_email, recipient_list)
        
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=user_name,password=password,email=email)
        user.save()

    return render(request, 'login.html')

def handlelogin(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print("not login")
            message="Invalid Credential"
            return render(request,'login.html',{"message":message})
    return render(request,'login.html')

        

def handlelogout(request):
    logout(request)
    return redirect('index')


def index2(request):
    return render(request, 'index2.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

def index5(request):
    return render(request, 'index5.html')


    