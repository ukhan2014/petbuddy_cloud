activate_this = '/home/ubuntu/petbuddy_cloud/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/html/petbuddy_cloud')

from petbuddy_cloud import app as application
