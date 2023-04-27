from django.shortcuts import render
from django.utils import timezone
from upload.models import UploadedImage
from .forms import SearchForm
from django.http import HttpResponse
from wsgiref.util import FileWrapper

import os



def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            matching_images = UploadedImage.objects.filter(tag1__icontains=query) | UploadedImage.objects.filter(tag2__icontains=query) | UploadedImage.objects.filter(tag3__icontains=query)
            no_match = False
            if not matching_images:
                no_match = True
            return render(request, 'db/results.html', {'matching_images': matching_images, 'no_match': no_match})
    else:
        form = SearchForm()
    return render(request, 'db/index.html', {'form': form})



