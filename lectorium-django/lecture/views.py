from django.shortcuts import render
from rest_framework import generics, viewsets
from account.models import *
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import math

class LectureListCreateView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    querysetFaculty = Faculty.objects.all()
    querysetCourse = Course.objects.all()
    querysetAccounts = Account.objects.all()
    serializer_class = LectureSerializer
    lookup_field = 'id'
    count_str = 0
    def get(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        querysetFaculty = super().get_queryset()
        querysetCourse = super().get_queryset()
        querysetAccounts = super().get_queryset()

        # Получаем параметры запроса
        title_lect = self.request.query_params.get('title_lect')
        limit = self.request.query_params.get('limit', 10)
        page = self.request.query_params.get('page', 1)
        teacher = self.request.query_params.get('teacher')
        cource = self.request.query_params.get('cource')
        faculty = self.request.query_params.get('faculty')
        date = self.request.query_params.get('date')
        #id_lect = self.request.query_params.get('id')
        
        count = queryset.count()
        start_index = (int(page) - 1) * int(limit)
        end_index = int(start_index) + int(limit)
        count_str = math.ceil(count / int(limit))

        if title_lect:
            queryset = queryset.filter(title_lect=title_lect)
        if teacher:
            teacher_instance = Account.objects.filter(vk_id=teacher).first()
            queryset = queryset.filter(lecturer=teacher_instance)
        if cource:
            course_instance = Course.objects.filter(title=cource).first()
            if course_instance:
                queryset = queryset.filter(cource=course_instance)
        if faculty:
            faculty_instance = Faculty.objects.filter(title=faculty).first()
            if faculty_instance:
                queryset = queryset.filter(faculty=faculty_instance)
        if date:
            queryset = queryset.filter(date=date)
        
        queryset = queryset[start_index:end_index]
        serializer = self.serializer_class(queryset, many=True)

        return Response({'data': serializer.data, 'total_pages': int(count_str)})
    
    
class LectureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    lookup_field = 'id'
    
class FacultyListCreateView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class FacultyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'id'
    
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'
    

    
    
#def download_file(request, pk):
    # Получить объект из базы данных по его ключу
    #file_object = Lecture.objects.get(pk=pk)
    # Получить путь к файлу из поля content
    #file_path = file_object.content.path
    # Открыть файл и прочитать его содержимое
    #with open(os.path.join(settings.MEDIA_ROOT, file_path), 'rb') as file:
        #response = HttpResponse(file.read(), content_type='text/html')
        #response['Content-Disposition'] = 'attached; filename=' + os.path.basename(file_path)
        #return response
    
