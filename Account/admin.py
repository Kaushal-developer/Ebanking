from django.contrib import admin
from .models import account_detail, loan_data

# Register your models here.
admin.site.register(account_detail)
admin.site.register(loan_data)