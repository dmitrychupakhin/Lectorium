from django.db import models
from account.models import *
import os

class Course(models.Model):
    title = models.TextField()
    def __str__(self):
        return self.title
    
class Faculty(models.Model):
    title = models.TextField()
    def __str__(self):
        return self.title
    
class Lecture(models.Model):
    title_lect = models.TextField()
    content = models.FileField(upload_to='media')
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    lecturer = models.ForeignKey(Account,on_delete=models.SET_NULL, null=True)
    cource = models.ForeignKey(Course,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title_lect

    

    
    