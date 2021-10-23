from rest_framework import serializers
from .models import OrderItem
from django.contrib.auth.models import User


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OrderItem