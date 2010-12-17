from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = []

# only serve non-fqdn URLs
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^dj_jsurls\.js$','dj_jsurls.views.dj_jsurl_list',name='dj_jsurls_list'),
        )

