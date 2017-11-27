from django.conf.urls import url

from .views import StaffListView, StaffDetailView, StaffCreateView

urlpatterns = [
    url(r'^create/$', StaffCreateView.as_view(), name="create"),
    url(r'^$', StaffListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', StaffDetailView.as_view(), name="detail"),

]



