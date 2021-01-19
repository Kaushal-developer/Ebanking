from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.db.models import Q
from twilio.rest import Client
import os
from pathlib import Path
from gtts import gTTS  
from django.conf import settings 
# Create your views here.
from django.core.files import File
from NovaScotia.models import Offeres
def home(request):
    if request.session.has_key('email'):
        try:
            user = request.session['email']
            z = Customer.objects.get(email=user)
            # say('Welcome to the bank of NovaScotia,\tMr.'+z.name)
            o = Offeres.objects.all()
            print(o)
            return render(request, 'index.html', {'z1': z.id,'o':o})
        except:
            return render(request, 'index.html',{'o':o})
    else:
        o = Offeres.objects.all()
        print(o)
        return render(request, 'index.html',{'o':o})

def login(request):
    if request.method == 'POST':
        print("done")
        if 'login' in request.POST:
            try:
                email = request.POST['email']
                password = request.POST['password']
                user = Customer.objects.get(email=email)
                print(user)
                if user.password == password:
                    request.session['email'] = email
                    print("loged")
                    return redirect('/home/')
                else:
                    # say('Wrong password')
                    messages.error(request, "Wrong Password")
                    return redirect('/login/')
            except:
                # say('Wrong Email address')
                messages.error(request, "Wrong Email Address")
                return redirect('/login/')
    return render(request, 'base.html')


def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
        # import os
        # try:
        #     os.remove('C:/Users/Acer/Downloads/python_django/billa/bank/static/voice/speech1.txt')
        #     os.remove('C:/Users/Acer/Downloads/python_django/billa/bank/static/voice/speech1.mp3')
        return redirect('/login/')
        # except:
        #     return redirect('/login/')
    else:
        return redirect('/login/')

def about(request):
    if request.session.has_key('email'):
        print('still in session')
        user = request.session['email']
        z = Customer.objects.get(email=user)
        print(z)
        return render(request, 'about.html', {'z': z, 'z1': z.id})
    else:
        return render(request, 'about.html')

def profile(request, id):
    if request.session.has_key('email'):
        user = get_object_or_404(Customer, id=id)
        print(user)
        return render(request, 'profile.html', {'user': user})

# Create your views here.
def signup(request):
    if request.method == 'POST':
        print('come')
        try:
            if 'DATA' in request.POST:
                name = request.POST['name1']
                mobile = request.POST['mobile']
                email = request.POST['email1']
                pass1 = request.POST['password1']
                pass2 = request.POST['password2']
                print(name, mobile, email, pass1)
                if pass1 == pass2:
                    Customer(name=name,email=email,mobile=mobile,password=pass1).save()
                    z = Customer.objects.get(email=email)       
                    print(z.id)         
                    print('done')               
                    global Z1
                    Z1 = Acgen(4, 'Here is Your OTP to register Your Account', 9427023068)
                    return redirect(f'/otp/{z.id}')
                else:
                    messages.error(request, 'Password Not Match')
                    return redirect('/signup/')
        except:
            messages.info(request, 'Check your connections')
            return redirect('/signup/')
    return render(request, 'signup.html')


def Acgen(x, y, z):
    num = '000111222333444555666777888999'
    ACN = ''.join(random.sample(num, x))
    account_sid = 'ACc91f501535b813d2e390#*#*#*#*#*#'
    auth_token = '38170dc2d5ee10385266727#*#*#*#*#*#'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=y + str(ACN),
        from_='+12059736191',
        to=f'+91{z}'
    )
    print(message.sid)
    return ACN


def otp(request,id):
    if request.method == 'POST':
        # say('Please enter the otp sent your account')   
        print(id) 
        Z2 = request.POST.get('n1')+request.POST.get('n2')+request.POST.get('n3')+request.POST.get('n4')
        print('inputed otp', Z2)
        print('generated OTP',Z1)
        if Z1 == Z2:
            try:
                messages.success(request, 'User created successfully')
                # say('user created Successfully')
                return redirect('/login/')
            except:
                Customer.objects.filter()
                # say('Email Address or mobile number already exists try again')
                messages.error(request, 'Email Address or mobile number already exists try again')
                return redirect('/signup/')
        else:
            # say('Invalid OTP entered!!!')
            messages.error(request, 'Invalid OTP')
            return redirect('/signup/')
    return render(request, "otpver.html")

# def say(x):
#     import pyttsx3
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 180)
#     a = 'C:/Users/Acer/Downloads/python_django/billa/bank/static/voice/speech1.txt'
#     f = open(a, 'w')
#     f.write(x)
#     f.close()
#     f = open(a, 'r')
#     theText = f.read()
#     f.close()
#     tts = gTTS(text=theText, lang='en')
#     tts.save('C:/Users/Acer/Downloads/python_django/billa/bank/static/voice/speech1.mp3')
#     print("File saved!")

def forget(request):
    if request.method =='POST':
        email = request.POST.get('email')
        mobile = request.POST.get('mob')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password1 == password2:
            z = Customer.objects.filter(Q(email=email) | Q(mobile=mobile)).update(password=password1)
            print(z)
            # say('password Updated')
            return redirect('/login/')
        else:
            return redirect('/forget/')
    return render(request, 'forget.html')
