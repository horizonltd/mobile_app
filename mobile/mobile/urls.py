
from django.contrib import admin
from django.urls import path, include

#Optional Imports
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [

    path('admin/', admin.site.urls),
    path('home', views.HomePage.as_view(), name='home'),
    # #This registered the hub url.py here
    path('api/v1/', include('schedule.urls')),
]
