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
    template_name = "form.html"
    form_class = AppraisalForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Create Review"
        return context


class AppraisalUpdateView(UpdateView):
    template_name = "form.html"
    form_class = AppraisalForm

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Update Review"
        return context
