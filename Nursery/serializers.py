from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Nursery.models import CustomUser,Plant, NurseryDetails




class UserRegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)
    password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role','password')
        extra_kwargs = {
            'password': {'write_only': True},

        }
        
    def create(self, validated_data):
        user = User(email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        div = CustomUser(user=user,role='User')
        div.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = authenticate(password=attrs['password'], username=attrs['username'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return attrs

    def create(self, validated_data):
        user = User.objects.get(username=validated_data['username'])
        return user
    
class PlantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plant
        fields = ['id','name']
        
        

class NurseryRegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)
    password = serializers.CharField(required=True, write_only=True)
    nurseryName = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role','password','nurseryName')
        extra_kwargs = {
            'password': {'write_only': True},

        }
        
    def create(self, validated_data):
        user = User(email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        div = CustomUser(user=user,role='NursuryOwner')
        transdiv = NurseryDetails(user=user , nurseryName=self.validated_data['nurseryName'])
        div.save()
        transdiv.save()
        return user