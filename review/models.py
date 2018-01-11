from django.conf import settings
from django.db import models

from staff.models import StaffProfile


class Appraisal(models.Model):
    # Associations
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    employee = models.ForeignKey(StaffProfile)
    # actual appraisal
    overall_rating = models.CharField(max_length=120)
    positive_qualities = models.TextField(blank=True)
    negative_qualities = models.TextField(blank=True)
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.employee.first_name

    def get_positive_q(self):
        return self.positive_qualities.split(",")

    def get_negative_q(self):
        return self.negative_qualities.split(",")








