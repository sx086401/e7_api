from django.db import models

class Characters(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField()
    element = models.CharField(max_length=50)
    star = models.IntegerField()
    role = models.CharField(max_length=50)
