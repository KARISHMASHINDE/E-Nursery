from django.shortcuts import render
from Nursery.functions import createResponse, get_tokens_for_user
from Nursery.serializers import UserRegisterSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User




# Create your views here.
class registration_view(APIView):
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            refresh = get_tokens_for_user(user)
            access = refresh['access']
        else:
            return createResponse(False, "Registration Failed", serializer.errors, "errors")
        return createResponse(True, "User Successfully Registered", {'details': serializer.data, 'access': access}, 'data')