from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('register/', views.register),
    path('login/', views.login),
    path('s_class/', views.s_class),
    path('t_activity/', views.t_activity),
]

handler404 = 'personal.views.error_404_view'