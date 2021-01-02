from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import os
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser



 

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


def authenticate_user(user, typ):
    if isinstance(user, AnonymousUser):
        return False
    if user.role != typ:
        return False
    return True


class IsUser(IsAuthenticated):
    def has_permission(self, request, view):
        if not authenticate_user(request.user, "User"):
            return False
        return bool(request.user)

