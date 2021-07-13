"""
WSGI config for to_do_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

curr_env = os.environ.get('DJANGO_ENV')
if curr_env == 'DEV':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'to_do_app.settings.development'
elif curr_env == 'PROD':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'to_do_app.settings.production'

application = get_wsgi_application()
