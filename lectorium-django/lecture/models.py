from django.db import models
import os

class Lecture(models.Model):
    title_lect = models.TextField()
    content = models.FileField(upload_to='media')
    faculty = models.TextField()
    lecturer = models.TextField()
    cource = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    