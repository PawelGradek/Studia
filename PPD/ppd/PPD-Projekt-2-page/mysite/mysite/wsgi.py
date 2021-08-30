"""
WSGI config for mysite project.

It exposes the WSGI callable as wypadly_teraz_i_w_pieciu_poprz module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.txt')

application = get_wsgi_application()
