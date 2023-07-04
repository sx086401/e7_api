from rest_framework import serializers
from .models.users import Users
from .models.characters import Characters

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

class CharacterSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Characters
        fields = ['id', 'name', 'image_url', 'element', 'star']

    def validate_element(self, value):
        if value not in ['fire', 'ice', 'earth', 'light', 'dark']:
          raise serializers.ValidationError('element is not valid')
        return value

