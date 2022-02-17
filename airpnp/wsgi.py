"""
WSGI config for airpnp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()

env = os.environ.get('ENV')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'airpnp.settings.{env}')

application = get_wsgi_application()
