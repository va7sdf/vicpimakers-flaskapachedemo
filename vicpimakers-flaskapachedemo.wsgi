python_home = '/var/www/vicpimakers-flaskapachedemo/venv'

import sys
import site

python_version = '.'.join(map(str, sys.version_info[:2]))
site_packages = python_home + '/lib/python%s/site-packages' % python_version

site.addsitedir(site_packages)

sys.path.insert(0, '/var/www/vicpimakers-flaskapachedemo')
from app import app as application

