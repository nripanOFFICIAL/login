from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')
def add(request):
    if request.method=="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        u_name=request.POST['u_name']
        email=request.POST['email']
        e_pass=request.POST['e_pass']
        c_pass=request.POST['c_pass']
        if e_pass==c_pass:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,'The user is exists already')
                return redirect('index')
            else:
                user=User.objects.create_user(first_name=f_name,last_name=l_name,username=u_name,email=email,password=c_pass)
                user.save()      
        else:
            messages.info(request,'Password is not matching!! ')
            return redirect('index')
        return redirect('login')
        
def login(request):
    return render (request,'login.html')

@login_required(login_url='login')
def afterlog(request):
    return render(request,'log.html')

def log(request):
    u_name=request.POST['u_name']
    e_pass=request.POST['e_pass']
    user=auth.authenticate(username=u_name,password=e_pass)
    if user is not None:
        auth.login(request,user)
        return redirect('afterlog')
    
def logout(request):
    return redirect(index)
    

