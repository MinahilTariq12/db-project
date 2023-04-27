from django.db import models
from upload.models import UploadedImage


class DownloadedImage(models.Model):
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    download_time = models.DateTimeField(auto_now_add=True)
