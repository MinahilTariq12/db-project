# In models.py of the upload_log app
from django.db import models
from django.utils import timezone
from upload.models import UploadedImage

class UploadLog(models.Model):
    uploaded_at = models.DateTimeField(default=timezone.now)
    uploaded_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
