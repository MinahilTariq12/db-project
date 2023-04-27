from django.urls import path
from .views import download_image



app_name = "download"


urlpatterns = [
    path('<int:image_id>/', download_image, name='download_image'),
]
