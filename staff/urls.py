from django.conf.urls import url
from . import views

from .views import (StaffListView, StaffCreateView, StaffUpdateView, StaffDeleteView)


urlpatterns = [
    url(r'^$', StaffListView.as_view(), name='list'),
    url(r'^create/$', StaffCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', StaffUpdateView.as_view(), name="detail"),
    url(r'^delete/(?P<pk>\d+)/$', StaffDeleteView.as_view(), name="delete")
    # url(r'^delete/(?P<slug>[\w-]+)/$', views.staff_delete, name='delete_employee'),
]



