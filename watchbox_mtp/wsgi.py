"""
WSGI config for watchbox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watchbox_mtp.settings')

application = get_wsgi_application()

# Delay migrations until registry is ready
def run_migrations():
    import threading
    from django.core.management import call_command
    try:
        call_command('migrate', interactive=False)
        print("Migrations applied successfully.")
    except Exception as e:
        print(f"Migration failed: {e}")

# Run in a background thread to avoid app registry issues
threading.Thread(target=run_migrations).start()