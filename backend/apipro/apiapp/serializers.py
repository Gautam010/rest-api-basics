from rest_framework import serializers
from django.db import models
from .models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields="__all__"
   

