from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Registration, User
from django.contrib import messages
from django.views import View

# Create your views here.
#1

class reg_dis(View):

    def get(self, request):
        fm = Registration()
        user = User.objects.all()
        return render(request, 'clasbv/reg&dis.html', {'foo': fm, 'user': user})


    def post(self, request):
         fm = Registration(request.POST)
         if fm.is_valid():
            nm = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password1']

            if User.objects.filter(email=em):
                messages.error(request, "E-mail already exists")

            else:

                reg = User(username=nm, email=em, password=pw)
                reg.save()
                fm = Registration()

         user = User.objects.all()
         return render(request, 'clasbv/reg&dis.html', {'foo': fm, 'user': user})


#2

class modify_data(View):

    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = Registration(instance=pi)
        return render(request, 'clasbv/modify.html', {'form': fm})


    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = Registration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

        return render(request, 'clasbv/modify.html', {'form': fm})

#3

class delete_data(View):

    def post(self, rerquest, id):
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/')