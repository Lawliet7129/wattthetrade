import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "energy_trading.core.settings")


application = get_wsgi_application()
