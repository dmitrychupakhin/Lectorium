from django.db import models
import os

class Lecture(models.Model):
    title = models.TextField()
    content = models.FileField(upload_to='media')

    