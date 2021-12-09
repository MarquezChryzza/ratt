from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from account.models import Account
from act.models import Activity
from personal.models import studentInfo


def error_404_view(request,exception):
    return render(request, 'project_name/404.html')

def home_screen_view(request):
    context = {}

    accounts = Account.objects.all()
    context['account'] = accounts


    return render(request, "account/login.html",  context)

def home(request):
    return render(request, 'personal/single-project.html')

def login(request):
    return render(request, '../templates/login.html')

def s_class(request):
    return render(request, '../templates/s_class.html')

def t_activity(request):
    data = Activity.objects.all()
    return render(request, '../templates/t_activity.html',{'data':data})

def register(request):
    return render(request, '../templates/register.html')



