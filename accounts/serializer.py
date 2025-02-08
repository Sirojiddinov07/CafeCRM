from rest_framework import serializers
from .models import Waiter

class WaiterRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class WaiterLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
