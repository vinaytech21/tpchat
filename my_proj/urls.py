from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import events.urls
import services.urls
import products.urls
import accounts.urls
import allauth.urls
import follow.urls
from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^account/', include('authtools.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^products/', include(products.urls, namespace='products')),
    url(r'^services/', include(services.urls, namespace='services')),
    url(r'^events/', include(events.urls, namespace='events')),
    url(r'^s/$', 'my_proj.views.search', name='search'),
    url(r'^z/$', 'my_proj.views.zipcode', name='zipcode'),
    url(r'^conect/$', 'my_proj.views.conect', name='conect'),
    url(r'^faq/$', 'my_proj.views.faq', name='faq'),
    url(r'^tour/$', 'my_proj.views.tour', name='tour'),
    url(r'^term/$', 'my_proj.views.term', name='term'),
    url(r'^contact/$','my_proj.views.contact', name='contact'),
    url(r'^messages/', include('django_messages.urls')),
    #url(r'^chat/', include('chatrooms.urls')),
    url(r'^follow/', include(follow.urls, namespace='follow')),
    url(r'^event/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    url(r'^service/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    url(r'product/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    #url(r'^avatar/', include('avatar.urls')),
    url(r'^avatar/', include('easy_avatar.urls')),
    #url(r'^chat/', include('djangotribune.urls')),
    url(r'^groupchat1/', include('chatroom.urls')),
    #tribune url(r'^chat/', include('djangoChat.urls')), 
    url(r'^zipuser/', 'my_proj.views.Zipuser', name='Zipuser'),
    url(r'^zipuserdetail/(?P<pk>[0-9]+)/$', 'my_proj.views.zipuserdetail', name='zipuserdetail'),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

