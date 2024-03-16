from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'id'

class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'id'
