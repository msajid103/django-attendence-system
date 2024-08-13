
from django.contrib import admin
from django.urls import path,include
from .view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('student/',include('dashboard.urls')),
]
