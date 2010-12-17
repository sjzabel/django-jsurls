from django.shortcuts import render_to_response
from dj_jsurls.models import get_named_urls
# Create your views here.

def dj_jsurl_list(request):
    return render_to_response(
                'dj_jsurls/dj_jsurl_list.html',
                {'named_urls': get_named_urls()},
                mimetype="application/javascript")
    
