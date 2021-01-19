from django.db import models

# Create your models here.
class account_detail(models.Model):
    date = models.DateField(auto_now=True)
    Aname= models.CharField(max_length=200)
    Fname = models.CharField(max_length=200)
    Mname = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    email = models.EmailField(primary_key=True, unique=True,)
    dob = models.CharField(max_length=200)
    mob = models.IntegerField()
    aadhar = models.IntegerField(unique=True)
    pancard = models.CharField(max_length=200,unique=True)
    account_type = models.CharField(max_length=200)
    Applicants_image = models.ImageField(upload_to='files/')
    aadhar_image = models.ImageField(upload_to='files/')
    pan_image = models.ImageField(upload_to='files/')
    Sign = models.ImageField(upload_to='files/')
    account_approve = models.CharField(max_length=20,default='pending')

    def __str__(self):
        return self.email 


class loan_data(models.Model):
    name= models.CharField(max_length=200)
    add = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    email = models.EmailField(primary_key=True, unique=True,)
    mob = models.IntegerField()
    A_image = models.ImageField(upload_to='files/')
    u_exists = models.CharField(max_length=5, default='No')
    emp_type = models.CharField(max_length=20)
    sal_range = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    loan_approve = models.CharField(max_length=20,default='pending')
    loan_type = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name
