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
import vk_api


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
                response_data = data.get('response', {})
                token = response_data.get('access_token', '')
                user_id = response_data.get('user_id', '')
                
                vk = vk_api.VkApi(token=token)
                vk_session = vk_api.VkApi(token=token)
                # Получение экземпляра API
                vk = vk_session.get_api()

                # Получение информации о пользователе
                user_info = vk.users.get(user_ids=user_id, fields=['first_name', 'last_name', 'photo_max_orig'])
                user = user_info[0]

                f_name = user['first_name']
                l_name = user['last_name']
                t_name = "ffe"
                ava = user.get('photo_max_orig')
                is_Prep = False
                is_Admin = False
                try:
                    account = Account.objects.get(vk_id=user_id)
                except Account.DoesNotExist:
                    account = Account.objects.create(
                        vk_id=user_id,
                        first_name=f_name,
                        last_name=l_name,
                        third_name=t_name,
                        avatar=ava,
                        is_Prepod=is_Prep,
                        is_Superuser=is_Admin
                    )
                    account.save()
                account = Account.objects.get(vk_id=user_id)
                is_P = account.is_Prepod
                is_A = account.is_Superuser
                return Response({'access_token': token, 'first_name':f_name,'last_name':l_name,'avatar':ava, 'is_user_teacher': is_P, 'is_user_super': is_A})
            else:
                return Response({'error': 'Failed to exchange silent token'})
        else:
            return Response({'title': 'title'})
        