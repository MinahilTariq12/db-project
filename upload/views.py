from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import UploadImageForm
from .models import UploadedImage
from upload_log.models import UploadLog

from django.core.files.base import ContentFile
from datetime import datetime

@require_POST
def upload_image(request):
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_image = form.save(commit=False)
        uploaded_image.image.save(request.FILES['image'].name, ContentFile(request.FILES['image'].read()))
        uploaded_image.save()

        # create a new upload log entry
        upload_log = UploadLog.objects.create(uploaded_image=uploaded_image)

        return render(request, 'upload/upload.html')    
    else:
        return render(request, 'upload/upload.html', {'form': form})

def upload(request):
    if request.method == 'POST':
        return upload_image(request)
    else:
        form = UploadImageForm()
        return render(request, 'upload/upload.html', {'form': form})
