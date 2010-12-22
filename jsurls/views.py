from django.shortcuts import render_to_response
from jsurls.models import get_named_urls
# Create your views here.

def jsurl_list(request):
    return render_to_response(
                'jsurls/jsurl_list.html',
                {'named_urls': get_named_urls()},
                mimetype="application/javascript")
    
