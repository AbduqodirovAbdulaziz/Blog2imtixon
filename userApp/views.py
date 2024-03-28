from django.shortcuts import render,redirect
from django.views import *
from django.contrib.auth import *



class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        user=authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request,user)
            return redirect('maqolalar')
        return redirect('login')



class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect()