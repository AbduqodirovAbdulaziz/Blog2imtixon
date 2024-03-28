from django.shortcuts import render,redirect
from django.views import View
from .models import *

class BlogView(View):
    def get(self,request):
        context={
            'maqolalar': Maqola
        }
        return render(request,'blog.html',context)

class BittaMaqola(View):
    def get(self,request,pk):
        context={
            "maqola":Maqola.objects.filter(id=pk)
        }
        return render(request,'bittaMaqola',context)