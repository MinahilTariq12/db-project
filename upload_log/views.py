from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import UploadLog

def log_upload(request):
    if request.method == 'POST':
        # Retrieve data from request
        image_id = request.POST.get('image_id')
        uploaded_at = request.POST.get('uploaded_at')

        # Create new UploadLog instance
        upload_log = UploadLog()
        upload_log.image_id = image_id
        upload_log.uploaded_at = uploaded_at
        upload_log.save()

        # Return success response
        return JsonResponse({'status': 'success'})

    # Return error response if request method is not POST
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
