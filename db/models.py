from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.db import models


class SearchHistory(models.Model):
    query = models.CharField(max_length=255)
    search_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.query
