from rest_framework import serializers
from .models import Waiter

class WaiterLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
