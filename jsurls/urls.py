import re
from django.conf import settings
from django.conf.urls.defaults import patterns, url, include
from django.core.exceptions import ImproperlyConfigured

urlpatterns = []

# only serve non-fqdn URLs
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^jsurls.js$', 'jsurls.views.jsurl_list',name='jsurls_list'),
    )

def jsurls_urlpatterns(prefix=None):
    """
    Helper function to return a URL pattern for serving the jsurls.js file.
    """
    if not settings.DEBUG:
        return []
    if prefix is None:
        prefix = settings.STATIC_URL
    if not prefix or '://' in prefix:
        raise ImproperlyConfigured(
            "The prefix for the 'jsurls_urlpatterns' helper is invalid.")
    if prefix.startswith("/"):
        prefix = prefix[1:]

    return patterns('',
        url(r'^%s' % re.escape(prefix), include(urlpatterns)),
    )
