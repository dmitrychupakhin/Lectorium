from django.db import models
import os

class Account(models.Model):
    vk_id = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    third_name = models.TextField()
    avatar = models.TextField()
    is_Prepod = models.BooleanField()
    is_Superuser = models.BooleanField()
