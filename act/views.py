from django.shortcuts import render
from django.contrib.auth import forms
from django.shortcuts import render, redirect
from .forms import ActivityForm
from django.contrib.auth.forms import AuthenticationForm
from .import models
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from act.models import Activity
from account.models import Account
from classroom.models import Classroom
from django.contrib import messages
# Create your views here.


def t_activity(request):

    submitted = False
    if request.method == "POST":
        form =ActivityForm(request.POST, request.FILES)
        if form.is_valid():
                if request.user.is_authenticated:
                 instance = form.save(commit=False)
                 messages.success(request, 'Your form was uploaded successfully!')
                 instance.clss = request.user.classroom
                 form.save()
                return HttpResponseRedirect('/t_activity?submitted=True')
    else: 
        form = ActivityForm()
        if request.user.is_authenticated:
            get_classroom = request.user.classroom
            act = Activity.objects.filter(clss = get_classroom)
        if 'submitted' in request.GET:
            submitted = True

    return render(request, '../templates/t_activity.html', {'form':form, 'submitted': submitted, 'act':act})

