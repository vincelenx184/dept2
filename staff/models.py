from django.db import models


class StaffProfile(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    profile_timestamp = models.DateTimeField(auto_now_add=True)
    profile_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

