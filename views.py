from multiprocessing import context
from django.shortcuts import redirect, render

def register(request):
    context = {}
    return render(request, 'newacustica/register.html', context)

def login_view(request):
    context = {}
    return render(request, 'newacustica/login.html', context)

def logout_view(request):
    context = {}
    return redirect('newacustica:login')