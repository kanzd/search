from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import *


from django.db.models import Q
from . import models
from . import serializer
class SearchAPI(APIView):
    def post(self,req):
        search=req.data['search']
        search_val = models.Search.objects.filter(Q(name__contains=search)|Q(items__contains=search)|Q(address__contains=search)|Q(pincode__contains=search))
        search_ser=serializer.SearchSerializer(search_val,many=True)
        return Response(search_ser.data)


class AddAPI(APIView):
    def post(self,req):
        rec=models.Search()
        rec.name=req.data['name']
        rec.items=req.data['items']
        rec.address=req.data['address']
        rec.pincode=req.data['pincode']
        rec.save()
        return Response({"message":"rec saved"})