from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fulishe.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    url(r'^joke/$', 'joke'),
    url(r'^joke/(\d+)$','morejoke'),
    url(r'^picture/$', 'picture'),
    url(r'^picture/(\d+)$','morepicture'),
    url(r'^video/$', 'video'),
    url(r'^video/(\d+)$','morevideo'),
    url(r'^album/$', 'album'),
    url(r'^album/(\d+)$','morealbum'),
    url(r'^album/beauty/(\d+)/(\d+)$','albumbeauty'),
    url(r'^album/video/(\d+)/(\d+)','albumvideo'),
    url(r'^album/pic/(\d+)/(\d+)$','albumpic'),

)