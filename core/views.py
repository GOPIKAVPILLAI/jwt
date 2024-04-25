from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer,LoginSerializer
from django.contrib.auth import authenticate
from .models import User
# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken


class Register(APIView):
    def get(self,request):
        objs=User.objects.all()
        serializer=UserSerializer(objs, many=True)
        return Response(serializer.data)
    def post(self,request):
        data=request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:  
            return Response(serializer.errors)

class Login(APIView):
    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        if serializer.is_valid():
            email=serializer.data['email']
            password=serializer.data['password']
            print(email)
            print(password)
            user=authenticate(request,email= email,password= password)
            print(user)
            if user is None:
                return Response({'error': 'User password is wrong'}, status=401)
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }
        else:
            return Response({'error': 'anonymous user'}, status=401)

