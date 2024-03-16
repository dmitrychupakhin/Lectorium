from .views import *
from django.urls import path

urlpatterns = [
    path('lecture/', LectureListCreateView.as_view()),
    path('lecture/<int:id>/', LectureRetrieveUpdateDestroyView.as_view() ),
    #path('lecture/download/<int:pk>/', download_file, name='download_file'),
]