from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from bank.models import Customer
from .models import account_detail, loan_data
import random
from twilio.rest import Client
from django.core.exceptions import ObjectDoesNotExist
import qrcode
from NovaScotia.models import AccountNumber, loan_approved_user
import base64
from django.db.models import Q
from bank.views import Acgen

# from bank.views import say


def a_ccount(request):
    if request.session.has_key('email'):
        email = request.session['email']
        z = Customer.objects.filter(email=email).get()
        print(z.id)
        try:
            print('checking for account')
            # say('Welcome to the account Section')
            x = account_detail.objects.filter(Q(account_approve='pending') | Q(
                account_approve='Approved'), email=email).get()
            print(x)
            return render(request, 'account.html', {'z': z.id, 'z1': x})
        except:

            return render(request, 'account.html', {'z': z.id})
    else:
        return render(request, 'account.html')


def acform(request, id):
    if request.session.has_key('email'):
        ema = request.session['email']
        user = get_object_or_404(Customer, id=id)
        try:
            queryset = get_object_or_404(account_detail, email=ema)
            print(queryset)
            if queryset:
                return redirect(f"/ACC_message/{id}")
        except:
            if request.method == 'POST':
                y = []
                list1 = ['Aname', 'Fname', 'Mname', 'address', 'state', 'city',
                         'pincode', 'email', 'dob', 'mob', 'aadhar', 'pan', 'ACC']
                for i in list1:
                    y.append(request.POST[i])
                Applicants_image = request.FILES.get('image_person')
                aadhar_image = request.FILES.get('image_aadhar')
                pan_image = request.FILES.get('image_pan')
                Sign = request.FILES.get('image_sign')
                if user.email == y[7]:
                    print('done')
                    account_detail(Aname=y[0], Fname=y[1], Mname=y[2], Address=y[3], state=y[4], city=y[5], pincode=y[6], email=y[7], dob=y[8], mob=y[9], aadhar=y[10],
                                   pancard=y[11], account_type=y[12], Applicants_image=Applicants_image, aadhar_image=aadhar_image, pan_image=pan_image, Sign=Sign).save()
                    z2 = '''\nWe have recieved Bank Account opening request.\nPlease wait for while until we check your data.'''
                    z3 = Acgen(0, z2, 9427023068)
                    messages.success(
                        request, 'Account data uploaded Successfully')
                    # say('You have successfully submited new bank account request')
                    return redirect(f"/ACC_message/{id}/")
                else:
                    messages.error(
                        request, 'EMAIL address or mobile number are not matched')
                    # say('Your email address or mobile number may not matching')
                    return redirect(f'/acform/{id}/')
            return render(request, 'accform.html', {'z': id})
    else:
        return render(request, 'accform.html')


def loan_det(request):
    if request.session.has_key('email'):
        email = request.session['email']
        z = Customer.objects.filter(email=email).get()
        print(z.id)
        try:
            print('checking for account')
            # say('Welcome to the account Section')
            x = loan_data.objects.filter(Q(loan_approve='pending') | Q(
                loan_approve='Approved'), email=email).get()
            print(x)
            return render(request, 'loan_detail.html', {'z': z.id, 'z1': x})
        except:
            return render(request, 'loan_detail.html', {'z': z.id})
    else:
        # say('welcome to the loan section')
        return render(request, 'loan_detail.html')


def loan_form(request, id):
    if request.session.has_key('email'):
        ema = request.session['email']
        print(ema)
        user = get_object_or_404(Customer, id=id)
        try:
            queryset = get_object_or_404(loan_data, email=ema)
            print(queryset)
            if queryset:
                return redirect(f"/loan_message/{id}")
        except:
            if request.method == 'POST':
                y = []
                list1 = ['exist_cust', 'Aname', 'address', 'state', 'city', 'pincode',
                         'email', 'mobile', 'loan_type', 'Employ_type', 'salary_range']
                for i in list1:
                    y.append(request.POST[i])
                print(y)
                applicants_image = request.FILES.get('image_person')
                if user.email == y[6]:  
                    print('done')
                    loan_data(name=y[1], add=y[2], state=y[3], city=y[4], pincode=y[5], email=y[6], mob=y[7],
                              loan_type=y[8], A_image=applicants_image, u_exists=y[0], emp_type=y[9], sal_range=y[10]).save()

                    return redirect(f"/loan_message/{id}/")
                else:
                    messages.error(
                        request, 'EMAIL address or mobile number are not matched')
                    return redirect(f'/loan_form/{id}/')
            return render(request, 'loan_form.html', {'z': id})
    else:
        return redirect('/login/')


def loan_calc(request):
    if request.method == "POST":
        p = float(request.POST.get('amount'))
        n = int(request.POST.get('months'))
        r = float(request.POST.get('rate1'))
        mrate = r/(12*100)
        print(p, r, n)
        z = (p*mrate*(1+mrate)**n)/(((1+mrate)**n)-1)
        return render(request, 'loan_calc.html', {'z': z})
    else:
        return render(request, 'loan_calc.html')


def mess(request, id):
    if request.session.has_key('email'):
        email = request.session['email']
        try:
            z11 = account_detail.objects.filter(
                account_approve='Approved', email=email).get()
            print(z11)
            if z11:
                z5 = AccountNumber.objects.get(email=email)
                print(z5, z5.Acount_number, z5.PIN)
                z1 = z5.Acount_number
                z2 = z5.PIN
                z7 = 'Name: ' + str(z5) + '\nAccount Number: ' + \
                    str(z1) + '\nYour Pin: '+str(z2)
                print(z7)
                messages.info(
                    request, 'Kindly scan this Qrcode to get info about your account.')
                return render(request, 'mess.html', {'z': id, 'z11': z11, 'z7': z7, 'z5': z5})
        except:
            messages.info(request, 'Wait for account apporval')
            return render(request, 'mess.html', {'z': id})
    else:
        return redirect('/home/')


def message1(request, id):
    if request.session.has_key('email'):
        email = request.session['email']
        print(email)
        try:
            z11 = loan_data.objects.filter(
                loan_approve='Approved', email=email).get()
            print(z11)
            if z11:
                z5 = loan_approved_user.objects.get(email=email)

                messages.info(
                    request, 'Kindly scan this Qrcode to get info about your account.')
                return render(request, 'loan_message.html', {'z': id, 'z11': z11, 'z5': z5})
        except:
            messages.info(request, 'Wait for account apporval')
            return render(request, 'loan_message.html', {'z': id})
    else:
        return redirect('/home/')


def captcha():
    alpha = 'qwertyuiopasdfghjklzxcvbnm'
    z = ''.join(random.sample(alpha, 5))
    return z
