from rest_framework import serializers
from .models import Menu
from django.db import models
from .models import Booking

class  MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'