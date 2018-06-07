"""
WSGI config for ProyectoSena project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

path = '/home/path/to/project'
if path not in sys.path:
    sys.path.append(path)
    sys.path.append('/home/django_projects/ProyectoSena')
	sys.path.append('/home/django_projects/ProyectoSena/ProyectoSena')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProyectoSena.settings")

application = get_wsgi_application()

