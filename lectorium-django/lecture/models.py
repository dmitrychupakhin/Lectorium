from django.db import models
import os

class Lecture(models.Model):
    title = models.TextField()
    content = models.FileField(upload_to='media')
    faculty = models.TextField()
    lecturer = models.TextField()
    cource = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)

    