import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "energy_trading.core.settings")





if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
