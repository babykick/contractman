#coding=utf-8
from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from project.views import DashboardView

# Create your views here.
class RegisterView(View):    
    def post(self, request):
        uf = UserForm(request.POST, prefix='user')
        upf = AuthorForm(request.POST, prefix='userprofile')
        if uf.is_valid() and upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return JsonResponse({'sucess':1, 'name':username})
        
 
class LoginView(View):
     """ 实现登录页面
     
     """
     
     def get(self, request):
         return render(request, 'account/login.html')
     
    
     def post(self, request):
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username, password=password)
         if user is not None:
            if user.is_active:
                 login(request, user)
                 return redirect('/dashboard/')
         else:
            return render(request)

