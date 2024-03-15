from rest_framework import serializers
from .models import *

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'content')
        read_only_fields = ('id',)