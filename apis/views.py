from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from . import models
from . import serializer
class SearchAPI(APIView):
    def post(self,req):
        search=req['search']
        search_val = models.Search.objects.filter(Q(name__contains=search)|Q(items__contains=search)|Q(address__contains=search)|Q(pincode__contains=search))
        search_ser=serializer.SearchSerializer(search_val,many=True)
        return Response(search_ser.data)
