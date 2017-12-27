from django.conf import settings
from django.db import models

from staff.models import StaffProfile


class Appraisal(models.Model):
    # Associations
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    employee = models.ForeignKey(StaffProfile)
    # actual appraisal
    overall_rating = models.CharField(max_length=120)
    positive_qualities = models.TextField
    negative_qualities = models.TextField
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

