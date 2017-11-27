from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import StaffProfile
from django.shortcuts import render, get_object_or_404
from .forms import StaffProfileCreateForm


class StaffListView(ListView):
    def get_queryset(self):
        return StaffProfile.objects.all()


class StaffDetailView(DetailView):
    queryset = StaffProfile.objects.all()


class StaffCreateView(CreateView):
    form_class = StaffProfileCreateForm
    template_name = "staff/form.html"

    def form_valid(self, form):
        instance = form.save()
        instance.save()
        return super(StaffCreateView, self).form_valid(form)








