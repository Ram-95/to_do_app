#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    curr_env = os.environ.get('DJANGO_ENV')
    if curr_env == 'DEV':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'to_do_app.settings.development'
    elif curr_env == 'PROD':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'to_do_app.settings.production'

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
