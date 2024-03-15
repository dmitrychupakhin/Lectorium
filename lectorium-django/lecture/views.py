from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
class LectureListCreateView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    lookup_field = 'id'

class LectureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    lookup_field = 'id'
    
def download_file(request, pk):
    # Получить объект из базы данных по его ключу
    file_object = Lecture.objects.get(pk=pk)
    # Получить путь к файлу из поля content
    file_path = file_object.content.path
    # Открыть файл и прочитать его содержимое
    with open(os.path.join(settings.MEDIA_ROOT, file_path), 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
        return response
    
