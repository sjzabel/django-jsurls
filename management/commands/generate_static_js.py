from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.template import Context
from django.template.loader import get_template

from optparse import make_option
import os

from jsurls.models import get_named_urls

class Command(BaseCommand):
    help  = 'Creates a static js file for production; Use setting DJ_JSURLS_PATH = "/home/me/site/static/js/"'

    option_list = BaseCommand.option_list + (
        make_option('--path',
            #action='change_path',
            dest='path',
            default='',
            help='Override the path set in Settings.'),
        )

    def _get_path(self,**options):
        path = ''

        if 'path' in options and options['path']!="":
            path = options['path']
        elif hasattr(settings,'DJ_JSURLS_PATH'):
            path = settings.DJ_JSURLS_PATH
        else:
            path = os.path.join(settings.STATIC_ROOT,'js')

        return path



    def handle(self, *args, **options):
        path = self._get_path(**options)
        
        if not os.path.exists(path):
            raise CommandError('Path "%s" does not exist' % path )
        
        outfile = open(os.path.join(path,'jsurls.js'),'w')

        template = get_template('jsurls/jsurl_list.html')
        print template

        outfile.write(
                template.render(
                    Context(
                        {'named_urls': get_named_urls()} )))
        outfile.close()

        self.stdout.write('Successfully wrote file to "%s"\n' % os.path.join(path,'jsurls.js'))

