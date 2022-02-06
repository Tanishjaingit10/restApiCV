
# from audioop import reverse
# from datetime import datetime
# import json
# from django.http import HttpResponseRedirect
# from oauth2_provider.models import AccessToken, Application
# from django.contrib.auth import authenticate,login
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ViewUsersAPIView(APIView):
    def get(self, req):
        users = User.objects.all()
        ser = UserSerilizer(users, many=True)
        for i in ser.data:
            del i["password"]
        return Response(ser.data)


class GetUserAPIView(APIView):
    def get(self, req, pk):
        try:
            user = User.objects.get(pk=pk)
            ser = UserSerilizer(user)
            data = ser.data
            del data["password"]
            return Response(data)
        except:
            return Response({})
        
class SignupAPIView(APIView):
    serializer_class = RegisterUserSerializer
    parser_classes = (MultiPartParser,)

    name = openapi.Parameter(name='name',in_=openapi.IN_FORM,type=openapi.TYPE_STRING,required=True)
    email = openapi.Parameter(name='email',in_=openapi.IN_FORM,type=openapi.TYPE_STRING,required=True)
    password1 = openapi.Parameter(name='password1',in_=openapi.IN_FORM,type=openapi.TYPE_STRING,required=True)
    password2 = openapi.Parameter(name='password2',in_=openapi.IN_FORM,type=openapi.TYPE_STRING,required=True)
    resume = openapi.Parameter(name="resume",in_=openapi.IN_FORM,type=openapi.TYPE_FILE,required=True)
    @swagger_auto_schema( manual_parameters=[name,email,password1,password2,resume])
    def post(self, req):
        ser = RegisterUserSerializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else: return Response(ser.errors)

class UpdateUserAPIView(APIView):
    serializer_class = UpdateUserSerializer
    def put(self,req,pk):
        try:
            user = User.objects.get(pk=pk)
            print(req.data)
        except:
            pass
        return Response(1000)

class ResumeAPIView(APIView):
    def get(self,req):
        resume = Resume.objects.all()
        ser = ResumeSerilizer(resume,many=True)
        return Response(ser.data)
