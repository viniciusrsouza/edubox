from rest_framework import serializers
from edubox.users.models import User

class CreateAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (['id',
                   'email',
                   'name',])
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (['id',
                   'email',
                   'name',])
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)