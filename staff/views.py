from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import StaffProfile
from django.shortcuts import render, get_object_or_404


class StaffListView(ListView):

    def get_queryset(self):
        return StaffProfile.objects.all()


class StaffDetailView(DetailView):
    queryset = StaffProfile.objects.all()






