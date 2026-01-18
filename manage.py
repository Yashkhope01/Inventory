#!/usr/bin/env python
import os
import sys

# Expose WSGI entrypoints for platforms (e.g. Vercel) that import this file
# and expect a module-level `app` or `handler` instead of running `main()`.
try:
    from amazon.wsgi import application as app  # noqa: E402
    handler = app
except Exception:
    # Keep CLI usage unaffected even if import fails in unusual environments.
    app = None
    handler = None

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
