from django.conf import settings
from django.core.urlresolvers import get_resolver

class JSUrl(object):
    def __init__(self,key,url_s,var_li):
        '''
        Right now this is kinda hacky... 
        there are a lot of variations of the same data that I use to build the js
        '''
        key = key.replace('-','_')
        self.path_key = key.replace('__',":")
        self.key = key 
        self.var_li = var_li
        self.url_s = url_s
        self.url_template = self.get_url_template(url_s)
        self.var_template = ",".join(self.var_li) 

    def get_url_template(self,s):
        template = "{{{{ {0} }}}}"
        d =  dict([(var,template.format(var)) for var in self.var_li])
        return s % d

    def __cmp__(self,other):
        return cmp(self.path_key,other.path_key)

    def __repr__(self):
        return self.path_key

from django.core.urlresolvers import RegexURLPattern,RegexURLResolver
from django.utils.regex_helper import normalize

def get_named_urls(include_admin=False):
    def _get_named_urls(resolver, ns="",pattern="",parts=None):
        if resolver.namespace:
            if not include_admin \
                    and ns=="" \
                    and resolver.namespace=='admin':return []
            if not ns=='':
                ns += "__"
            ns += resolver.namespace

        if not parts:
            parts = []

        norml = normalize(resolver.regex.pattern)
        if len(norml)>1: raise Exception('jsurls currently can only deal with a single path')
        norml = norml[0]

        _pattern,_parts = norml
        pattern += _pattern 

        parts.extend(_parts)

        rslts=[]    
        for r in resolver.url_patterns:
            if r.__class__==RegexURLResolver:
                rslts.extend(_get_named_urls(r,ns=ns,pattern=pattern,parts=parts))

        for p in resolver.url_patterns:
            if p.__class__==RegexURLPattern and p.name and p.name!="":
                name = ns and ns or ""
                if not name=="":
                    name += '__'
                name += p.name

                norml = normalize(p.regex.pattern)
                if len(norml)>1: raise Exception('jsurls currently can only deal with a single path')
                norml = norml[0]

                _pattern,_parts = norml

                _pat = pattern + _pattern 

                _par = []
                _par.extend(parts)
                _par.extend(_parts)

                rslts.append(JSUrl(name,_pat,_par))

        return rslts


    resolver = get_resolver(settings.ROOT_URLCONF)
    rslt = sorted(_get_named_urls(resolver))

    return rslt 


