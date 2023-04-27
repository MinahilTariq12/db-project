from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import DownloadedImage
from upload.models import UploadedImage



def download_image(request, image_id):
    downloaded_image = DownloadedImage.objects.create(image_id=image_id)
    image = get_object_or_404(UploadedImage, pk=image_id)
    response = HttpResponse(image.image, content_type='image/jpeg')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(image.image.name)
    return response
