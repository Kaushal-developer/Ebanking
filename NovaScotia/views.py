from django.shortcuts import render, get_object_or_404,redirect
from bank.models import Customer
from Account.models import account_detail, loan_data
from .models import AccountNumber, Administrative,loan_approved_user,Offeres
import random
from twilio.rest import Client
from django.contrib import messages
# Create your views here.
import datetime
from bank.views import Acgen

def home_admin(request):
    if request.session.has_key('email'):
        z = Customer.objects.all()
        print(z)
        return render(request, 'admin_base.html', {'z': z})
    else:
        return redirect('/login_admin/')

def Account_status(request):
    if request.session.has_key('email'):
        z = account_detail.objects.all().filter(account_approve='pending')
        print(z)
        return render(request, 'account_status.html', {'z': z})
    else:
        return redirect('/login_admin/')

def Loan_status(request):
    if request.session.has_key('email'):
        z = loan_data.objects.all().filter(loan_approve='pending')
        print(z)
        return render(request, 'loan_status.html', {'z': z})
    else:
        return redirect('/login_admin/')

def view_det(request, e):
    if request.session.has_key('email'):
        z = get_object_or_404(account_detail, email=e)
        print(z.Aname)
        return render(request, 'view.html', {'z': z})
    else:
        return redirect('/login_admin/')    

def loan_view(request, e):
    if request.session.has_key('email'):
        z = get_object_or_404(loan_data, email=e)
        print(z.name)
        return render(request, 'view_loandata.html', {'z': z})
    else:
        return redirect('/login_admin/')

def Approve_acc(request, e):
    if request.session.has_key('email'):
        z = account_detail.objects.filter(
            email=e).update(account_approve='Approved')
        print(z)
        if z is not False:
            print(z)
            z2='''Your Account Activated Successfully Please visit once in account Section to know your account details'''
            z1 = Acgen(0,z2,9427023068)
            print('message sent')
            z = get_object_or_404(account_detail, email=e)
            print(z)
            A,B=acc_numbergen(12,6)
            print(A,B)
            z10=AccountNumber(Name=z.Aname,Acount_number=A,PIN=B,email=e,mob=z.mob)
            z10.save()
            print('data saved')
            return redirect('/home_admin/')
        return render(request, 'Approve.html', {'z': z})
    else:
        return redirect('/login_admin/')

def Disapprove_acc(request, e):
    if request.session.has_key('email'):
        z = account_detail.objects.filter(
            email=e).update(account_approve='Disapproved')
        if z is not False:
            print(z)
            z2='''Your Account Disapproved due to mismatch in DATA.'''
            z1 = Acgen(0,z2,9427023068)
            print('message sent')
        return render(request, 'Approve.html')
    else:
        return redirect('/login_admin/')

def Approve_loan(request, e):
    if request.session.has_key('email'):    
        z = loan_data.objects.filter(
            email=e).update(loan_approve='Approved')
        print('loan Approved')
        if z is not False:
            
            print(z)
            z2='''Your loan has been approved Successfully Please visit once in loan Section to know your loan details'''
            z1 = Acgen(0,z2,9427023068)
            A,B=acc_numbergen(12,6)
            z3 = get_object_or_404(loan_data,email=e)
            loan_approved_user(Name=z3.name,account_ID=A,pin=B,EMI=10000,email=z3.email,loan_type=z3.loan_type,mob=z3.mob).save()
            print('message sent')
            return redirect('/home_admin/')
        return render(request, 'Disapprove.html', {'z': z})
    else:
        return redirect('/login_admin/')

def Disapprove_loan(request, e):
    if request.session.has_key('email'):
        z = loan_data.objects.filter(
            email=e).update(loan_approve='Disapproved')
        if z is not False:
            print(z)
            z2='''Your loan hasbeen Disapproved due to lower cibil score'''
            z1 = Acgen(0,z2,9427023068)
            print('message sent')
        return render(request, 'Disapprove.html')
    else:
        return redirect('/login_admin/')

def login_admin(request):
    if request.method == 'POST':
        print("done")
        try:
            email = request.POST['ema']
            password = request.POST['pas']
            user = Administrative.objects.get(email=email)
            print(user)
            if user.password == password:
                request.session['email'] = email
                print("loged")
                request.session['email'] = email
                return redirect('/home_admin/')
            else:
                messages.error(request, "Wrong Password")
                return redirect('/login_admin/')
        except:
            messages.error(request, "Wrong Email Address")
            return redirect('/login_admin/')
    return render(request, 'login_admin.html')

def signup_admin(request):
    if request.method == 'POST':
        print('come')
        try:
            if 'sub' in request.POST:
                name = request.POST['name']
                mobile = request.POST['mob']
                email = request.POST['ema']
                pass1 = request.POST['pass1']
                pass2 = request.POST['pass2']
                print(name, mobile, email, pass1)
                if pass1 == pass2:
                    global Z1
                    Z1 = Acgen(4, 'Here is Your OTP to register Your Account', 9427023068)
                    return redirect(f'/otpverify/{name}/{mobile}/{email}/{pass1}/')
                else:
                    messages.error(request, 'Password Not Match')
                    return redirect('/signup_admin/')
        except:
            messages.info(request, 'Check your connections')
            return redirect('/signup_admin/')
    return render(request, 'signup_admin.html')

def otpverify(request,x,y,z,w):
    if request.method == 'POST':   
        print(x,y,z,w) 
        Z2 = request.POST.get('n1')+request.POST.get('n2')+request.POST.get('n3')+request.POST.get('n4')
        print('inputed otp', Z2)
        print('generated OTP',Z1)
        if Z1 == Z2:
            print('otp checked')
            try:
                Administrative(Name=x, mob=y,email=z, password=w).save()
                messages.success(request, 'User created successfully')
                return redirect('/login_admin/')
            except:
                messages.error(request, 'Email Address or mobile number already exists try again')
                return redirect('/signup_admin/')
        else:
            messages.error(request, 'Invalid OTP')
            return redirect('/signup_admin/')
    return render(request, "otpverify.html")


def acc_numbergen(x,y):
    num = '000111222333444555666777888999'
    acn = ''.join(random.sample(num, x))
    print(acn)
    p= ''.join(random.sample(num,y))
    return acn,p

def logout_admin(request):
    if request.session.has_key('email'):
        del request.session['email']
        return redirect('/login_admin/')
    else:
        return redirect('/login_admin/')


def deals(request):
    if request.session.has_key('email'):
        if request.method == 'POST':
            head = request.POST.get('heading')
            des = request.POST.get('desc')
            date_time = request.POST.get('datetime')
            Pic = request.FILES.get('pic')
            print(head,des,date_time,Pic)
            try:
                Offeres(heading=head,desc=des,pic=Pic).save()
                print("done")
                return redirect('/home_admin/')
            except:
                print('error')
                return render(request, 'deals.html')
        return render(request, 'deals.html')
    else:
        return redirect('/login_admin/')
        
def deals_view(request):
    if request.session.has_key('email'):
        z = Offeres.objects.all()
        return render(request, 'deals_view.html',{'z':z})
    else:
        return redirect('/login_admin/')


def deals_update(request,id):
    if request.session.has_key('email'):
        z = get_object_or_404(Offeres, pk=id)
        print(z)
        if request.method == 'POST':
            z.heading = request.POST.get('heading')
            z.desc = request.POST.get('desc')
            z.pic = request.FILES.get('pic')
            z.save()
            return redirect('/deals_view/')
        return render(request,'deals.html',{'z':z})
    else:
        return redirect('/login_admin/')

def deals_delete(request,id):
    if request.session.has_key('email'):
        z = get_object_or_404(Offeres, pk=id)
        Offeres.objects.filter(offer_id=id).delete()
        return redirect('/deals_view/')
    else:
        return redirect('/login_admin/')