from rest_framework import serializers
from .serializers import *
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('vk_id', 'first_name', 'last_name','third_name','avatar','is_Prepod', 'is_Superuser')
        read_only_fields = ('id',)