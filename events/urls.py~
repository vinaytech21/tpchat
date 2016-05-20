from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.event, name='event'),
    url(r'^active/$',views.active, name='active'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.event_detail, name='event_detail'),
    url(r'^host/$', views.host, name='host'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.host_detail, name='host_detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.host_edit, name='host_edit'),
    url(r'^history/$', views.devent_detail, name='devent_detail'),
    url(r'^(?P<pk>[0-9]+)/public/$', views.event_public_list, name='event_public_list'),
]
