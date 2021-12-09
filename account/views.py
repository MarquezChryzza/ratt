from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, Student
from django.contrib.auth.backends import ModelBackend

def registration_view(request):

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            account = authenticate(username=username,password = password)
            login(request, account, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)            



def logout_view(request):
    logout(request)
    return redirect('/')



def login_view(request):
    
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("login")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                if user.is_student:
                    return redirect('s_class/')
                if user.is_teacher:
                    return redirect('t_activity/')

    else:
        form =AccountAuthenticationForm()


    context['login_form'] = form
    return render(request, 'account/login.html', context)    



