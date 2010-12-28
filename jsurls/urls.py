from django.conf import settings
from django.conf.urls.defaults import patterns,url

from jsurls.views import jsurl_list

urlpatterns = []
def jsurls_urlpatterns(js_dir_name='js'):
    """
    Helper function to return a URL pattern for serving the jsurls.js file.
    """
    if not settings.DEBUG:
        return []
    
    prefix = "%s/%s" % ('static_js_urls',js_dir_name)
    
    return patterns('',
        url(r'^%s/jsurls\.js$' % prefix,jsurl_list, name="jsurls"),
    )
