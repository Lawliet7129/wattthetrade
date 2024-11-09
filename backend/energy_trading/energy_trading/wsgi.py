import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'energy_trading.energy_trading.settings')

application = get_wsgi_application()
