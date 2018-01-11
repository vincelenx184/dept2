from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Appraisal
from .forms import AppraisalForm


class AppraisalListView(ListView):

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)


class AppraisalDetailView(DetailView):

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)


class AppraisalCreateView(CreateView):
    form_class = AppraisalForm

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)


class AppraisalUpdateView(UpdateView):
    form_class = AppraisalForm

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)
