# from django.contrib import messages

import re
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# from .forms import myform
from . models import ContactUs, Signup_login
def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contactus.html')

def logins(request):
    return render(request,'login.html')
    
def signup(request):
    return render(request,'signup.html')

def saveContactus(request):
    if request.method=="POST":
        name=request.POST.get('c_name')
        email=request.POST.get('c_email')
        m_num=request.POST.get('c_number')
        messg=request.POST.get('c_msg')
        c_data=ContactUs(name=name,email=email,m_num=m_num,messg=messg)
        c_data.save()
    return render(request, 'index.html')

def savesignup(request):
    if request.method=="POST":
        fname=request.POST.get('s_fname')
        lname=request.POST.get('s_lname')
        email=request.POST.get('s_email')
        psswd=request.POST.get('s_passwd')
        c_data=Signup_login(fname=fname,lname=lname,email=email,psswd=psswd)
        c_data.save()
    return render(request, 'login.html')

def savelogin(request):
    if request.method=='POST':
        email=request.POST.get('l_email')
        password=request.POST.get('password')
    return render(request, 'index.html')