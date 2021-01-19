from django.urls import path,include
from . import views
app_name = 'Account'

urlpatterns = [
    path('account/', views.a_ccount, name='account'),
    path('acform/<int:id>/',views.acform, name='acform'),
    path('loan_detail/', views.loan_det, name='loan_detail'),
    path('loan_calc/', views.loan_calc, name='loan_calc'),
    path('loan_form/<int:id>/', views.loan_form, name='loan_form'),
    path('ACC_message/<int:id>/', views.mess, name="mess" ),
    path('loan_message/<int:id>/', views.message1, name="loan_message" )
]
