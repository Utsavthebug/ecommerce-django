from django.shortcuts import render

from accounts.models import Account
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create(first_name=first_name,last_name=last_name,email=email,username=username)
            user.phone_number = phone_number
            user.set_password(password)
            user.save()
           
    context = {
        'form':form
    }
    return render(request,'accounts/register.html',context)

def login(request):
    return render(request,'accounts/login.html')


def logout(request):
    return render(request,'accounts/logout.html')


