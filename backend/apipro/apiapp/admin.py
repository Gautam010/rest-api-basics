from django.contrib import admin
from .models import *
@admin.register(Students)
# Register your models here.
class StudntsAdmin(admin.ModelAdmin):
  list_display=['id','name','roll','city']