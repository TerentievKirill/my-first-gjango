from django.db import models
from django.utils import timezone


class Device (models.Model):
    Name = models.CharField(max_length=200)
    Place = models.CharField(max_length=200)
    DT = models.DateTimeField(default=timezone.now)
    Indication = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Name
