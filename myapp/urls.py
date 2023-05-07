from django.urls import path
from . import views

urlpatterns = [
    path('home1/', views.home1, name='home1'),
    path('home2/', views.home2, name='home2'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('signin/', views.signin, name='signin'),
    path('signuppage/', views.signuppage, name='signuppage'),
    path('signup/', views.signup, name='signup'),
    path('info/', views.info, name='info'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('updatenumber/', views.updatenumber, name='updatenumber'),
    path('updateemail/', views.updateemail, name='updateemail'),
    path('updatepassword/', views.updatepassword, name='updatepassword'),
    path('listform/', views.listform, name='listform'),
    path('predicted/', views.predicted, name='predicted'),
]