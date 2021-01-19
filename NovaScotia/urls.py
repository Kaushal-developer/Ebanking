from django.urls import path,include
from . import views
app_name = 'NovaScotia'

urlpatterns = [
    path('home_admin/', views.home_admin, name='home_admin'),
    path('account_status/', views.Account_status, name='Account_status'),
    path('Loan_status/', views.Loan_status, name='loan_status'),
    path('view/<str:e>/', views.view_det, name='view'),
    path('loan_view/<str:e>/', views.loan_view, name='loan_view'),
    path('approve/<str:e>/', views.Approve_acc, name='approve'),
    path('Dispprove/<str:e>/', views.Disapprove_acc, name='Disapprove'),
    path('approve_loan/<str:e>/', views.Approve_loan, name='approve_loan'),
    path('Dispprove_loan/<str:e>/', views.Disapprove_loan, name='Disapprove_loan'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('signup_admin/', views.signup_admin, name='signup_admin'),
   path('otpverify/<str:x>/<int:y>/<str:z>/<str:w>/', views.otpverify, name='otpverify'),
    path('logout_admin/', views.logout_admin, name="logout_admin"),
    path('deals_admin/', views.deals, name='deals'),
    path('deals_view/', views.deals_view, name='deals_view'),
    path('deals_update/<int:id>/', views.deals_update, name='deals_update'),
    path('deals_delete/<int:id>/', views.deals_delete, name='deals_delete'),
]  