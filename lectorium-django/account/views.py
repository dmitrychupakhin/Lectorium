from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


# Create your views here.
class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'id'

class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'id'

class AccountloginView(APIView):
    def get(self, request):
        return Response({'title': 'title'})

    def post(self, request):
        if 'silent' and 'uuid' in request.data:
            # Получение данных из запроса
            silent = request.data['silent']
            version = '5.131'  # Версия API ВКонтакте
            app_service_token = '747f47b2747f47b2747f47b2177768de727747f747f47b2118a1d6de7a48d410d20e55d'
            uuid = request.data['uuid']

            # Вызов метода auth.exchangeSilentAuthToken
            response = requests.post('https://api.vk.com/method/auth.exchangeSilentAuthToken', data={
                'v': version,
                'token': silent,
                'access_token': app_service_token,
                'uuid': uuid
            })
            # Обработка ответа
            if response.status_code == 200:
                data = response.json()
                print(data)
                if 'access_token' in data:
                    access_token = data['access_token']
                    return Response({'access_token': access_token})
                else:
                    return Response({'error': 'Access token not found in response'})
            else:
                return Response({'error': 'Failed to exchange silent token'})
        else:
            return Response({'title': 'title'})
        