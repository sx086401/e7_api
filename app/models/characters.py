from django.db import models

class Characters(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField()
