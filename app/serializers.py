from rest_framework import serializers
from .models.state_details import StateDetails
from .models.states import States
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
        fields = ['id', 'name', 'image_url', 'element', 'star', 'classes']

    def validate_element(self, value):
        if value not in ['fire', 'ice', 'earth', 'light', 'dark']:
            raise serializers.ValidationError('element is not valid')
        return value

    def validate_classes(self, value):
        if value not in ['warrior', 'knight', 'thief', 'ranger', 'mage', 'soul_weaver']:
            raise serializers.ValidationError('classes is not valid')
        return value


class StateDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = StateDetails
        fields = [
            'id',
            'atk',
            'defense',
            'health',
            'spd',
            'cri',
            'crd',
            'eff',
            'res',
            'weapon',
            'helmet',
            'armor',
            'necklace',
            'ring',
            'boots',
            'weaponSet',
            'helmetSet',
            'armorSet',
            'necklaceSet',
            'ringSet',
            'bootsSet',
            'set1',
            'set2',
            'set3'
          ]

class StateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    current_state = StateDetailSerializer()
    expect_state = StateDetailSerializer()
    character_id = serializers.IntegerField()


    class Meta:
        model = States
        fields = ['id', 'character_id', 'character', 'current_state', 'expect_state', 'editor']
        depth = 1

    def create(self, validated_data):
        current_state_data = validated_data.pop('current_state')
        expect_state_data = validated_data.pop('expect_state')
        character_id = validated_data.pop('character_id', None)

        character = Characters.objects.get(id=character_id)
        current_state = StateDetails.objects.create(**current_state_data)
        expect_state = StateDetails.objects.create(**expect_state_data)
        states = States.objects.create(character=character, current_state=current_state, expect_state=expect_state, **validated_data)

        return states

    def update(self, instance, validated_data):
        current_state_data = validated_data.pop('current_state', None)
        expect_state_data = validated_data.pop('expect_state', None)
        character_id = validated_data.pop('character_id', None)

        if character_id:
          character = Characters.objects.get(id=character_id)
          instance.character = character

        current_state = instance.current_state
        current_state.__dict__.update(**current_state_data)
        current_state.save()

        expect_state = instance.expect_state
        expect_state.__dict__.update(**expect_state_data)
        expect_state.save()

        instance.__dict__.update(**validated_data)
        instance.save()

        return instance
