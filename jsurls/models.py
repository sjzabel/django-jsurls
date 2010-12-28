from django.conf import settings
from django.core.urlresolvers import get_resolver

class JSUrl(object):
    def __init__(self,key,url_s,var_li):
        '''
        Right now this is kinda hacky... 
        there are a lot of variations of the same data that I use to build the js
        '''
        key = key.replace('-','_')
        self.key = key 
        self.var_li = var_li
        self.url_s = url_s
        self.url_template = self.get_url_template(url_s)
        self.var_template = ",".join(self.var_li) 

    def get_url_template(self,s):
        template = "{{{{ {0} }}}}"
        d =  dict([(var,template.format(var)) for var in self.var_li])
        return s % d

def get_named_urls():
    resolver = get_resolver(settings.ROOT_URLCONF)
    rev_d = resolver._get_reverse_dict()
    return [JSUrl(k,*v[0][0]) for k,v in rev_d.items() if k.__class__==str]
