from django.conf.urls import url


from .views import (StaffListView, StaffCreateView, StaffUpdateView, StaffDeleteView, PractCreate)


urlpatterns = [
    url(r'^$', StaffListView.as_view(), name='list'),
    url(r'^create/$', StaffCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', StaffUpdateView.as_view(), name="detail"),
    url(r'^delete/(?P<pk>\d+)/$', StaffDeleteView.as_view(), name="delete"),


    # practice urls and slug round 2 from cfe

    #   url(r'^practice/(?P<pract_id>[\w-]+)/$', PractDetailView.as_view()),
    #   url(r'^practice/create/$', pract_create),


    url(r'^practice/create/$', PractCreate.as_view(), name="pract-create"),


]



