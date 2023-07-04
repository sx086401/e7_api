from rest_framework import serializers
from .models.users import Users

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Users
        fields = ['id', 'name', 'password', 'is_active', 'created_at']

class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    password = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Users
        fields = ['id', 'name', 'password', 'is_active', 'created_at']
