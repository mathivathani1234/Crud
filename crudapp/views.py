from django.shortcuts import render,redirect,get_list_or_404
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def login(request):
    if request.method == "POST":
        phone = request.POST.get('number')
        password=request.POST.get('password')
        print(phone,password)
        user_auth=auth.authenticate(username=phone,password=password)
        print("USER_AUTH",user_auth)
        if user_auth is not None:
             auth.login(request ,user_auth )
             print(user_auth)
             messages.success(request, 'Auth User')
             return redirect('/show')
        else:
           messages.success(request, 'User not found')
           return redirect('/')
    return render(request,'login.html')
def register(request):
   if request.method == "POST":
      if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.get(username =request.POST['uname'])
            return render(request, 'register.html' ,{'error': "User name Has been Taken"})
        except User.DoesNotExist:
            user = User.objects.create_user( username=request.POST['number'],first_name=request.POST ['uname'],email=request.POST['email'],password=request.POST['password1'])
            user.save()
            auth.login(request,user)
            return redirect('/')
      else:
            return render(request,'register.html',{'error': "Password Does Not Match"})
   else: 
       return render(request,'register.html')
@login_required
def show(request):
   A_USER = request.user
   if request.method == "POST":
        crudapp= request.POST.get('crudapp')
        print(crudapp)
        if crudapp is not None:
            crudapp_item = CrudappModel(crudapps=crudapp,user=request.user)
            crudapp_item.save()
            # print(crudapp_item)
   get_crudapp =CrudappModel.objects.filter(user=request.user)
   return render(request,'show.html',{'get_item':get_crudapp,'A_USER':A_USER})
def logout(request):
    auth.logout(request)
    return redirect('/')
def delete(request,id):
   crudapp_delete = CrudappModel.objects.get(id=id)
   print(crudapp_delete)
   crudapp_delete.delete()
   return redirect('/show')
def edit(request,id):
   if request.method=="POST":
       crudapp= request.POST.get('crudapp')
       # AUTH USER GET ID
       crudapp_obj = CrudappModel.objects.get(id=id)
       # For storing the value in particular field in
       # in Todo Model 'todos' field.
       crudapp_obj.crudapps=crudapp
       crudapp_obj.save()
       print ("Crudapp",crudapp,"CRUDAPPS" ,crudapp_obj)
       return redirect('/show')
   else:
       # Return the particular value with id.
       crudapp = CrudappModel.objects.filter(id=id)
       return render(request,'edit.html',{'crudapp':crudapp})
