from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Appraisal
from .forms import AppraisalForm
from django.urls import reverse_lazy


class AppraisalListView(ListView):

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)


# class AppraisalDetailView(DetailView):
#
#     def get_queryset(self):
#         return Appraisal.objects.filter(user=self.request.user)


class AppraisalCreateView(LoginRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = AppraisalForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Create Review"
        return context


class AppraisalUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "review/detail-update.html"
    form_class = AppraisalForm

    def get_queryset(self):
        return Appraisal.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Update Review"
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class AppraisalDeleteView(DeleteView):
    model = Appraisal
    template_name = "review/detail-update.html"
    success_url = reverse_lazy("review:list")
