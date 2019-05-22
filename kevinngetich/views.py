from django.views.generic import TemplateView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect

class home(TemplateView):
    template_name = 'home.html'

class login(TemplateView):
    template_name = 'login.html'

def logout(request):
    auth_logout(request)
    return redirect('/feed')