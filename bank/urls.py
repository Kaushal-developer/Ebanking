from django.urls import path,include
from . import views
app_name= 'bank'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('otp/<int:id>/', views.otp, name='otp'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('forget/', views.forget, name='forget')
    ]