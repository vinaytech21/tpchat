from django.conf.urls import patterns, include, url
from . import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import  servicelistListView

urlpatterns = patterns('services.views',    
    url(r'^$', servicelistListView.as_view(), name='servicelist'),
    url(r'^active/$', 'active', name='active'),
    url(r'^service/(?P<pk>[0-9]+)/$', 'service_detail_home', name='service_detail_home'),
    url(r'^offer/$', 'offer', name='offer'),
    url(r'^(?P<pk>[0-9]+)/edit/$', 'edit_service', name='edit_service'),
    url(r'^offer/(?P<pk>[0-9]+)/$', 'offer_detail_service', name='offer_detail_service'),
    url(r'^(?P<pk>[0-9]+)/public/$', views.service_public_list, name='service_public_list'),
    url(r'^history/$', 'service_history', name='service_history')
)  
