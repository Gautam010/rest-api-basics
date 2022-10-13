
from django.contrib import admin
from django.urls import path,re_path
from apiapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('det/<int:pk>',studetail),
    path('det/',stulist)
]
