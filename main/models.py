from django.db import models

# Create your models here.


class Cursor(models.Model):
    value = models.IntegerField()


class Data_wo_to_en(models.Model):
    wolof = models.TextField()
    english = models.TextField()
    is_translate = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
