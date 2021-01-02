from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import os
from rest_framework.response import Response



 

def get_tokens_for_user(user):
    refresh = AuthTokenObtainPairSerializer.get_token(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        obj = User.objects.get(pk=user.id)
        return token
    
    
    
    
def createResponse(status, message, data, typeOfData):
    msg = {"status": status, "message": message}
    return Response({"message": msg, typeOfData: data})



