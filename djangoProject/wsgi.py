"""
WSGI config for djangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi """
import os
import sys

try:
  sys.path.remove('/usr/lib/python3/dist-packages')
except:
  pass

sys.path.append('/home/c/cq29540/eqwr/public_html/paymentsNotifications/djangoProject/')
sys.path.append('/home/c/cq29540/eqwr/venv/lib/python3.6/site-packages/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
