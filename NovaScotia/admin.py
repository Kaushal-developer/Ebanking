from django.contrib import admin
from .models import AccountNumber,Administrative,Offeres,loan_approved_user
# Register your models here.
admin.site.register(AccountNumber)
admin.site.register(Administrative)
admin.site.register(Offeres)
admin.site.register(loan_approved_user)