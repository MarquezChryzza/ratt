from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


from personal.views import (
    home,
    t_activity,
)

from account.views import (
    login_view,
    logout_view,
    registration_view

)

from act.views import(
    t_activity,
)

from convert.views import(
   showvideo,
   savevideo,  
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('', login_view, name='login'),
    path('home/', home),
    path('t_activity/', t_activity),
    path('display/', showvideo, name='show'),
    path('s_class/', savevideo),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
