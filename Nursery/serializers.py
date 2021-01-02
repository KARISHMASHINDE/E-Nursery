from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Nursery.models import CustomUser,Plant, NurseryDetails, NurseryPlant




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
        
class NurseryDetailsGetSerializer(serializers.ModelSerializer):   
    class Meta:
        model = NurseryDetails
        fields = ['id','nurseryName','user']
        
        

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
        div = CustomUser(user=user,role='NurseryOwner')
        transdiv = NurseryDetails(user=user , nurseryName=self.validated_data['nurseryName'])
        div.save()
        transdiv.save()
        return user
    
class AddPlantSerializer(serializers.ModelSerializer):
    nurseryName = serializers.IntegerField(required=True,write_only=True)
    plant = serializers.IntegerField(required=True,write_only=True)
    price = serializers.FloatField(required=True)
    image = serializers.ImageField(required=True)
    class Meta:
        model = NurseryPlant
        fields = ['id', 'nurseryName', 'plant', 'image', 'price']
        
    def create(self, validated_data):

        self.nurseryName = NurseryDetails.objects.get(id=self.validated_data['nurseryName'])
        self.plant = Plant.objects.get(id=self.validated_data['plant'])
        transdiv = NurseryPlant(nurseryName=self.nurseryName,
                                image=self.validated_data['image'],
                                plant=self.plant,
                                price=self.validated_data['price'],)
        transdiv.save()
        return transdiv
    

    
    
class GetNurseryPlant(serializers.ModelSerializer):
    nurseryName = NurseryDetailsGetSerializer()
    plant = PlantSerializer()

    class Meta:
        model = NurseryPlant
        fields = ['id', 'image', 'price', 'nurseryName', 'plant']