# Deploy to PythonAnywhere (100% Free Forever)

## 1. Create Free Account
- Go to https://www.pythonanywhere.com/registration/register/beginner/
- Sign up (no credit card needed)

## 2. Setup Your Web App
1. Go to **Web** tab → **Add a new web app**
2. Choose **Manual configuration** → **Python 3.11**
3. Note your web app URL: `yourusername.pythonanywhere.com`

## 3. Upload Your Code
Open a **Bash console** and run:
```bash
git clone https://github.com/Yashkhope01/Inventory.git
cd Inventory
```

## 4. Install Dependencies (No Virtual Environment Needed)
```bash
# Remove any broken venv
rmvirtualenv clothing-env 2>/dev/null || true
deactivate 2>/dev/null || true

# Install using system pip3.11 with --user flag
cd ~/Inventory
/usr/bin/python3.11 -m pip install --user -r requirements.txt
```

## 5. Setup Environment (Free Tier - SQLite)
**For free tier, we'll use SQLite (no database service needed):**

```bash
cd ~/Inventory
export DJANGO_SECRET_KEY='abc123xyz789simplekey'
# No DATABASE_URL needed - will use default SQLite
```

## 6. Run Migrations
```bash
cd ~/Inventory
/usr/bin/python3.11 manage.py migrate
/usr/bin/python3.11 manage.py collectstatic --no-input
/usr/bin/python3.11 manage.py createsuperuser
```

## 7. Configure WSGI
Go to **Web** tab → **WSGI configuration file** → click to edit

Replace ALL content with:
```python
import os
import sys

# Add project directory to path
path = '/home/YOURUSERNAME/Inventory'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables (SQLite - no DATABASE_URL needed)
os.environ['DJANGO_SETTINGS_MODULE'] = 'amazon.settings'
os.environ['DJANGO_SECRET_KEY'] = 'abc123xyz789simplekey'
# DATABASE_URL not set - will use default SQLite database

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Replace `YOURUSERNAME` with your actual username and update DATABASE_URL.

## 8. Configure Static Files
In **Web** tab → **Static files** section, add:
- URL: `/static/`
- Directory: `/home/YOURUSERNAME/Inventory/staticfiles`

## 9. Set Virtual Environment
In **Web** tab → **Virtualenv** section:
- **Leave this field EMPTY** (we're using system Python with --user packages)

## 10. Reload Web App
Click the big green **Reload** button

Your app will be live at: `https://yourusername.pythonanywhere.com`

## Updating Your App
```bash
cd ~/Inventory
git pull
pip install -r requirements.txt
/usr/bin/python3.11 -m pip install --user -r requirements.txt
/usr/bin/python3.11 manage.py migrate
/usr/bin/python3.11

Then reload from Web tab.

## Free Tier Limits
- 512 MB disk space
- 100,000 requests/day
- 1 web app
- MySQL database included
- No credit card needed
- **No expiration - free forever!**
