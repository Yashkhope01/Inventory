#!/usr/bin/env python
import os
import sys

# Add the project root to sys.path to ensure module resolution works
# regardless of how the script is invoked.
current_path = os.path.dirname(os.path.abspath(__file__))
if current_path not in sys.path:
    sys.path.append(current_path)

# Set Django settings before any imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')

# Expose WSGI entrypoints for hosts that import this file directly (e.g. Vercel)
try:
    from amazon.wsgi import application as app
    handler = app
except Exception as e:
    import sys
    print(f"Serverless import failed (ignoring): {e}", file=sys.stderr)
    # Fallback: create a dummy WSGI app to satisfy Vercel's variable check.
    # This prevents the "Missing variable 'handler' or 'app'" error during build/scan.
    # Since traffic is routed to api/index.py, this dummy app won't actually handle requests.
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

