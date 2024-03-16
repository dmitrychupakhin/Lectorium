from rest_framework import serializers
from .models import *

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title_lect', 'faculty','lecturer','cource','content')
        read_only_fields = ('id',)