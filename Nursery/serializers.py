from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate




class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')
        extra_kwargs = {
            'password': {'write_only': True},

        }
        
    def create(self, validated_data):
        user = User(email=self.validated_data['email'], username=self.validated_data['username'], role='User',
                        QRCode=self.validated_data['phone'])
    password = self.validated_data['password']
    user.set_password(password)
    user.save()