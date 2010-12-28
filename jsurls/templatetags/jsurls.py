from django import template
from django.conf import settings

register = template.Library()
@register.tag(name="get_jsurls_static_prefix")
def do_render_jsurls_static_prefix(parser,token):
    return RenderStaticPrefixNode()

class RenderStaticPrefixNode(template.Node):
    def render(self,context):
        if settings.DEBUG:
            return '/static_js_urls/'
        else:
            if 'STATIC_PREFIX' in context:
                return "/%s" % context["STATIC_PREFIX"]
            else:
                return ''

