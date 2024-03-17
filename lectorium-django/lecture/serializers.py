from rest_framework import serializers
from .models import *
from account.serializers import *
from account.models import Account

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('title',)
        #read_only_fields = ('id',)
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title',)
        #read_only_fields = ('id',)
        
class LectureSerializer(serializers.ModelSerializer):
    faculty = serializers.CharField(source='faculty.title')
    cource = serializers.CharField(source='cource.title')
    lecturer = serializers.SerializerMethodField()
    class Meta:
        model = Lecture
        fields = ('id', 'title_lect', 'faculty','lecturer','cource','content')
        read_only_fields = ('id',)
    
    def get_lecturer(self, obj):
        if obj.lecturer:
            return f"{obj.lecturer.first_name} {obj.lecturer.last_name}"
        else:
            return None
    
        
        

        