from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import  ProductDetailView, ProductListView
from . import views

urlpatterns = patterns('products.views',        
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^post/$', views.list, name='list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail_list, name='post_detail_list'),
    #url(r'^list/detail/$', views.list_detail, name='list_detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.post_edit_list, name='post_edit_list'), 
    url(r'^history/$', 'post_history', name='post_history'),
    url(r'^detail/product/(?P<pk>[0-9]+)/$', 'post_detail_history', name='post_detail_history'),



)

