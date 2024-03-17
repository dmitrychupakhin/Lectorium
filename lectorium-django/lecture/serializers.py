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

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name')
        #read_only_fields = ('id',)
  
class LectureSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()
    cource = CourseSerializer()
    lecturer = LecturerSerializer()
    class Meta:
        model = Lecture
        fields = ('id', 'title_lect', 'faculty','lecturer','cource','content', 'date')
        read_only_fields = ('id',)
    
    
        
        

        