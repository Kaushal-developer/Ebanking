from django.db import models

# Create your models here.
class AccountNumber(models.Model):
    Name=models.CharField(max_length=100)
    Acount_number = models.IntegerField(unique=True)
    PIN = models.IntegerField(unique=True)
    email = models.EmailField(unique=True, primary_key=True)
    mob = models.IntegerField(unique=True)
    balance = models.FloatField(default=0)
    def __str__(self):
        return self.Name

class Administrative(models.Model):
    Name=models.CharField(max_length=100)
    email = models.EmailField(unique=True, primary_key=True)
    mob = models.IntegerField(unique=True)
    password = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.Name

class Offeres(models.Model):
    offer_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=5000)
    pic = models.ImageField(upload_to='events/') 
    
    def __str__(self):
        return self.heading

class  loan_approved_user(models.Model):
    Name = models.CharField(max_length=100)
    loan_type = models.CharField(max_length=100)
    loan_amount = models.FloatField(default=100000)
    years = models.IntegerField(default=1)
    EMI = models.FloatField()
    email = models.EmailField(unique=True, primary_key=True)
    mob = models.IntegerField(unique=True)
    rate = models.FloatField(default=7)
    account_ID = models.BigIntegerField(default=0)
    pin= models.IntegerField(default=0)
    def __str__(self):
        return self.Name