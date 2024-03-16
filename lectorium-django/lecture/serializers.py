from rest_framework import serializers
from .models import *
from account.serializers import *

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'title')
        read_only_fields = ('id',)
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')
        read_only_fields = ('id',)
        
class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title_lect', 'faculty','lecturer','cource','content')
        read_only_fields = ('id',)
        
    
        
        

        