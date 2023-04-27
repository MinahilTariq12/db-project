from django.db import models

class UploadedImage(models.Model):
    tag1 = models.CharField(max_length=100)
    tag2 = models.CharField(max_length=100)
    tag3 = models.CharField(max_length=100)
    image = models.ImageField()
