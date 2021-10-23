from rest_framework import serializers
from .models import ShippingAddress
from django.contrib.auth.models import User


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ShippingAddress