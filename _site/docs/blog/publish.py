import os
import sys
import shutil
import datetime

now = datetime.datetime.now()
month = now.strftime('%b').lower()
dir = "%s/%s/%s/" % (now.year, month, now.day)

os.system('mkdir -p %s' % dir)
shutil.copy(sys.argv[1], dir)
