from django.conf.urls import url
from . import views

from .views import (StaffListView, StaffCreateView, StaffUpdateView, StaffDeleteView, PractDetailView)


urlpatterns = [
    url(r'^$', StaffListView.as_view(), name='list'),
    url(r'^create/$', StaffCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', StaffUpdateView.as_view(), name="detail"),
    url(r'^delete/(?P<pk>\d+)/$', StaffDeleteView.as_view(), name="delete"),


    # practice urls and slug round 2 from cfe

    url(r'^practice/(?P<rest_id>\w+)/$', PractDetailView.as_view()),

]



