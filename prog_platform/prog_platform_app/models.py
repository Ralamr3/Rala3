from django.db import models

# Create your models here.

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    release_year = models.IntegerField()
    paradigm = models.CharField(max_length=200)
    typical_use = models.CharField(max_length=200)
