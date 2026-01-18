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

## 4. Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.11 clothing-env
pip install -r requirements.txt
```

## 5. Setup Database
In **Databases** tab:
- Initialize MySQL database (free)
- Note the database name, username, and password

Update settings in Bash console:
```bash
export DATABASE_URL="mysql://USERNAME:PASSWORD@USERNAME.mysql.pythonanywhere-services.com/USERNAME$clothing_shop"
export DJANGO_SECRET_KEY="10*%=xd%nkhy8r_c)uv*^09ve0!qdtvqkno8cwp&(j4x7d4ako"
```

## 6. Run Migrations
```bash
cd ~/Inventory
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py createsuperuser
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

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'amazon.settings'
os.environ['DJANGO_SECRET_KEY'] = '10*%=xd%nkhy8r_c)uv*^09ve0!qdtvqkno8cwp&(j4x7d4ako'
os.environ['DATABASE_URL'] = 'mysql://USERNAME:PASSWORD@USERNAME.mysql.pythonanywhere-services.com/USERNAME$clothing_shop'

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
- Enter: `/home/YOURUSERNAME/.virtualenvs/clothing-env`

## 10. Reload Web App
Click the big green **Reload** button

Your app will be live at: `https://yourusername.pythonanywhere.com`

## Updating Your App
```bash
cd ~/Inventory
git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
```

Then reload from Web tab.

## Free Tier Limits
- 512 MB disk space
- 100,000 requests/day
- 1 web app
- MySQL database included
- No credit card needed
- **No expiration - free forever!**
