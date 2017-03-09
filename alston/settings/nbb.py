"""
settings module for nbb

set env var
DJANGO_SETTINGS_MODULE=alston.settings.nbb
"""

DB_USER = 'root'
DB_PWD = 'mysql'
DB_HOST = 'localhost'

from alston.settings.base import *

import django
django.setup()

for db in DATABASES:
		DATABASES[db]['USER'] = DB_USER
		DATABASES[db]['PASSWORD'] = DB_PWD
		DATABASES[db]['HOST'] = DB_HOST
