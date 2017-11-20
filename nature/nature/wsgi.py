"""
WSGI config for nature project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

import sys

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/soleeh/Documents/moringacore-friday-ips/Django/IP1/Nature-clicks/nature")
os.environ["DJANGO_SETTINGS_MODULE"] = 'nature.settings'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nature.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)
