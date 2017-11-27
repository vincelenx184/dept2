from django.conf.urls import url

from .views import StaffListView, StaffDetailView

urlpatterns = [
    url(r'^$', StaffListView.as_view(), name='list'),
    #url(r'^(?P<slug>[\w]+)/$', StaffDetailView.as_view(), name="detail"),

]



