from django.shortcuts import render
from rest_framework.views import APIView
from api.serializer import Signup
from rest_framework.response import Response

# Create your views here.
class SignupView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Signup(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
