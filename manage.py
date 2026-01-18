#!/usr/bin/env python
import os
import sys

# Expose WSGI entrypoints for hosts that import this file directly (e.g. Vercel)
try:
    from amazon.wsgi import application as app  # noqa: E402
    handler = app
except Exception:
    app = None
    handler = None

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

