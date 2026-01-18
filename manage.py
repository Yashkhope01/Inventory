#!/usr/bin/env python
import os
import sys

# Define module-level variables FIRST so Vercel sees them even if import fails
app = None
handler = None

# Add the project root to sys.path to ensure module resolution works
# regardless of how the script is invoked.
current_path = os.path.dirname(os.path.abspath(__file__))
if current_path not in sys.path:
    sys.path.append(current_path)

# Set Django settings before any imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')

# Expose WSGI entrypoints for hosts that import this file directly (e.g. Vercel)
try:
    from amazon.wsgi import application
    app = application
    handler = application
except Exception as e:
    # Fallback: create a dummy WSGI app to satisfy Vercel's variable check.
    def dummy_app(environ, start_response):
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [b"manage.py is not a valid entry point. Check logs."]
    app = dummy_app
    handler = dummy_app

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

