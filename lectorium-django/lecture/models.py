from django.db import models

class Lecture(models.Model):
    title = models.TextField()
    content = models.TextField()
    