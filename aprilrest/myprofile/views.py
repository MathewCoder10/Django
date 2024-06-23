from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import userprofile
from. serializers import userser
# Create your views here.

class Take(APIView):
    def get(self,request,key):
        takepro=userprofile.objects.get(id=key)
        takeall=userser(takepro)
        return Response(takeall.data)
    
    def delete(self,request,key):
        takepro=userprofile.objects.get(id=key)
        takepro.delete()
        return Response('Data deleted')
    def put(self,request,key):
        userupdata=userprofile.objects.get(id=key)
        takendata=userser(userupdata,request.data)
        if takendata.is_valid():
            takendata.save()
            return Response(takendata.data)
        else:
            return Response('invalid updation')

class  takeprofile(APIView):
    def post(self,request):
        takepro=userser(data=request.data)
        if takepro.is_valid():
            takepro.save()
            return Response(takepro.data)
        else:
            return Response('invalid insertion')
        
        
    
