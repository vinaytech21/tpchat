from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import events.urls
import services.urls
import products.urls
import accounts.urls
from . import views


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^products/', include(products.urls, namespace='products')),
    url(r'^services/', include(services.urls, namespace='services')),
    url(r'^events/', include(events.urls, namespace='events')),
    url(r'^faq/$', 'my_proj.views.faq', name='faq'),
    url(r'^term/$', 'my_proj.views.term', name='term'),
    url(r'^contact/$','my_proj.views.contact', name='contact'),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^event/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    url(r'^service/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    url(r'product/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),

]



# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
