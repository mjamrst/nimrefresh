from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contact.views.home', name='home'),            
    url(r'^contact', 'contact.views.contactus', name='contactus'),
    url(r'^about-us/', 'contact.views.about', name='about'),
    url(r'^campaigns/', 'contact.views.campaigns', name='campaigns'),
    url(r'^pricing/', 'contact.views.pricing', name='pricing'),
    url(r'^thank-you/$', 'contact.views.thanks', name='thanks'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)