from django.views import View
from django.views.generic import TemplateView, ListView
from .models import StaffProfile


class StaffListView(ListView):

    def get_queryset(self):
        return StaffProfile.objects.all()




